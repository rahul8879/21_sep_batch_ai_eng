from openai import OpenAI
from dotenv import load_dotenv
import json
load_dotenv()


client = OpenAI()

def call_llm(prompt):
    response = client.chat.completions.create(
        model = "gpt-4o",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=10
    )
    return response.choices[0].message.content


