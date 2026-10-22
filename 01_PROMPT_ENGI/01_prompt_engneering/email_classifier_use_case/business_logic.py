from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI
import os
import time

client = OpenAI()

def call_llm(prompt,retires = 3):
    for attempt in range(retires):
        try:
            response = client.chat.completions.create(
                model = "gpt-4o-mini",
                messages=[{'role':'user',"content":prompt}]
            )
            return response.choices[0].message.content

        except Exception as e:
            error = str(e)

            if "401" in error or "authentication" in error.lower():
                return "AUTH ERROR"
            
            if "400" in error or "invalid request" in error.lower():
                return "INVALID REQUEST"
            
            # Rate limit or server error --> wait and retry
            wait = 2** attempt
            time.sleep(wait)



def load_prompt(filename):
    path = os.path.join('prompts',filename)
    # print('path',path)

    with open(path,'r') as f:
        return f.read()
    

# result = load_prompt("dummy.txt")
# print(result)

def classify_with_cot(subject,body,sender):
    template = load_prompt("classify_cot.md")
    prompt = template.format(subject=subject,body=body,sender=sender)
    result = call_llm(prompt)
    # print(result)
    # print('type of result', type(result))
    # return result
    for line in result.split('\n'):
        if "CATEGORY" in line:
            category =line.split(":")[1].strip()

        if "URGENCY" in line:
            urgency = line.split(":")[1].strip()

    return {
        "category": category,
        "urgency": urgency
    }

# dummy email

subject = "Meeting Reminder"
body = "Don't forget about the meeting tomorrow at 10 AM."
sender = "john.doe@example.com"

print(classify_with_cot(subject, body, sender))
