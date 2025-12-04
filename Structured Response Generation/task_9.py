import os
import requests
import json
import re
import sys
from typing import Dict, Any


API_KEY = os.getenv("GEMINI_API_KEY") or ""
MODEL = "gemini-pro"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"


def call_gemini(prompt: str, debug: bool = False) -> Dict[str, Any]:

    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ]
    }

    try:
        resp = requests.post(URL, headers=headers, json=payload, timeout=30)
    except requests.RequestException as e:
        return {"error": f"Request failed: {e}"}

    if debug:
        print(f"\nHTTP status: {resp.status_code}\n")


    try:
        body = resp.json()
    except ValueError:
        return {"error": "Response is not valid JSON", "text": resp.text}

    if debug:
        print("\nFULL API RESPONSE:\n")
        print(json.dumps(body, indent=2, ensure_ascii=False))
        print("\n--- end full response ---\n")

    return body


def extract_text_from_response(body: Dict[str, Any]) -> str:
 
    try:
   
        return body["candidates"][0]["content"]["parts"][0]["text"]
    except Exception:
     
      
        def walk(d):
            if isinstance(d, str):
                return [d]
            if isinstance(d, dict):
                out = []
                for v in d.values():
                    out.extend(walk(v))
                return out
            if isinstance(d, list):
                out = []
                for v in d:
                    out.extend(walk(v))
                return out
            return []

        texts = walk(body)
     
        if texts:
            texts = [t.strip() for t in texts if t and isinstance(t, str)]
            if texts:
                texts.sort(key=len, reverse=True)
                return texts[0]
        return "ERROR: Could not extract text from API response"


def safe_json_parse(text: str) -> Dict[str, Any]:

    try:
        parsed = json.loads(text)
        if isinstance(parsed, dict):
            return parsed
    except Exception:
        pass

    match = re.search(r'\{(?:.|\s)*\}', text)
    if match:
        candidate = match.group()
    
        candidate_fixed = re.sub(r',\s*}', '}', candidate)
        candidate_fixed = re.sub(r',\s*\]', ']', candidate_fixed)
        try:
            parsed = json.loads(candidate_fixed)
            if isinstance(parsed, dict):
                return parsed
        except Exception:
            pass

 
    lines = [ln.strip(' -•\t') for ln in text.splitlines() if ln.strip()]
    
    short = [ln for ln in lines if len(ln.split()) <= 12][:3]
    if len(short) >= 1:
      
        defaults = [
            "Easy syntax and readability",
            "Rich data science libraries (pandas, numpy, scikit-learn)",
            "Large and active community"
        ]
        benefits = short + defaults[len(short):]
        return {"benefits": benefits[:3], "note": "Used line-extraction fallback"}


    return {
        "benefits": [
            "Easy syntax and readability",
            "Rich data science libraries (pandas, numpy, scikit-learn)",
            "Large and active community"
        ],
        "warning": "Used default fallback because model output could not be parsed."
    }


def main():
    if API_KEY == "YOUR_API_KEY_HERE" or not API_KEY:
        print("ERROR: No API key found. Set the GEMINI_API_KEY environment variable or edit the script.")
        sys.exit(1)

    prompt = (
        "Respond ONLY in valid JSON format.\n\n"
        "Question: List 3 benefits of Python for data science.\n\n"
        "Return exactly this structure:\n"
        "{\n  \"benefits\": [\"...\", \"...\", \"...\"]\n}\n\n"
        "Do not include any extra commentary outside the JSON object."
    )

  
    raw_body = call_gemini(prompt, debug=True)

    if "error" in raw_body:
        print("\nAPI call error:", raw_body["error"])
        if "text" in raw_body:
            print("Raw text returned:", raw_body["text"])
        sys.exit(1)

    model_text = extract_text_from_response(raw_body)
    print("\nRAW MODEL TEXT:\n", model_text)


    final_json = safe_json_parse(model_text)

    print("\nFINAL PARSED JSON:\n", json.dumps(final_json, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
