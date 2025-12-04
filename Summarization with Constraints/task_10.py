import re



def paragraph_limit(summary):
 
    sentences = re.split(r'(?<=[.!?])\s+', summary.strip())

    if len(sentences) >= 2:
        sentence1 = sentences[0]
        sentence2 = sentences[1]
    else:
        return summary  
    combined = sentence1 + " " + sentence2
    word_count = len(combined.split())

    if word_count <= 50:
        return combined
    if len(sentence1.split()) <= 50:
        return sentence1  
     
    words = combined.split()
    return " ".join(words[:50])




summary = """In today's fast-paced world, staying informed is more important than ever. With the rise of digital media, people have access to a vast array of information at their fingertips. However, this abundance of """



print(paragraph_limit(summary))
