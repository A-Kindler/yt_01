import pandas as pd
import random
from openai import OpenAI

#topics = pd.read_csv(".../response.txt", sep = ".")# list of random topics

#response_collector = pd.DataFrame(columns=["ID","text"])

api_key="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"

prompt = str("Write a script for a short video (a short film). The video should be about 2 minutes long and tell a story about breaking up. The story should grab the viewer's attention right away and have the dramatic arc of a classic drama. No one says anything; everything is conveyed through actions. Feel free to be extreme in order to express something. Create a total of 6 scenes, each with only one cut. Submit only a table with the following content: scene_no; title; location; action; mood-visual highlight.")

def chat_request(prompt,model="gpt-4.1",max_tokens=300,temperature=0.7):
    client = OpenAI(api_key=api_key)
    chat_completion =client.chat.completions.create(
        model=model ,
        messages=[
            {"role": "system", "content":  "You are a helpful assistant."},
            {"role": "user", "content": prompt }
            ],

        max_tokens=max_tokens,
        temperature=temperature
        )
    answer = str(response.choices[0].message.content.strip().str.replace('\n', ' ', regex=False))
    print(answer)
    return answer

chat_request(prompt)






