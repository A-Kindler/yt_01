import pandas as pd
import random
from openai import OpenAI

topics = pd.read_csv(".../response.txt", sep = ".")# list of random topics

response_collector = pd.DataFrame(columns=["ID","text"])

api_key="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"
client = OpenAI(api_key=api_key)
prompt = str("Write a script for a short video (a short film). The video should be about 2 minutes long and tell a story about breaking up. The story should grab the viewer's attention right away and have the dramatic arc of a classic drama. No one says anything; everything is conveyed through actions. Feel free to be extreme in order to express something. Create a total of 6 scenes, each with only one cut. Submit only a table with the following content: scene_no; title; location; action; mood-visual highlight.")

chat_completion =client.chat.completions.create(
    model="gpt-4.1" ,
    messages=[
        {"role": "system", "content":  "You are a helpful assistant."},
        {"role": "user", "content": prompt }
        ],

    max_tokens=200,
    temperature=0.7
    )
answer = str(response.choices[0].message.content.strip())
print(answer)

response_collector["text"]=response_collector["text"].str.replace('\n', ' ', regex=False)

response_collector.to_csv(".../synth_safe.csv", index=False)



