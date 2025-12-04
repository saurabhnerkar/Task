import pandas as pd
import re


def clean_text(df):
    def clean(text):
        text = text.lower()
        text = re.sub(r'[^a-z0-9\s]', '', text)
        tokens = text.split()
        return tokens
    
    df['cleaned_text'] = df['text'].apply(clean)
    return df


df =pd.DataFrame({
    'text': [

        "hiii this is sample data///",
        "hello buddy@ this is python code%@!@",
        "&$hello word **!"

     
    ]
})


print("before clean", df)

print("after clean", clean_text(df))