from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import PydanticOutputParser
from typing import Literal
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(model_name="gpt-4o-mini")

class EmailClassification(BaseModel):
    category : Literal['Billing','Technical','Feature request','Other'] = Field(description='the category of the support email')
    urgency: Literal['High', 'Medium', 'Low'] = Field(
        description='Urgency based on business impact'
    )

    confidence: int = Field(
        description='Confidence score from 1 to 10',
        ge=1,   # ge = greater than or equal (Pydantic v2!)
        le=10   # le = less than or equal
    )

    resoning: str = Field(description="Once sentence explaination of the classiifcation")



parser = PydanticOutputParser(pydantic_object=EmailClassification)

cot_prompt = ChatPromptTemplate.from_messages([
    ('system', '''You are an expert support email classifier.

Classification Rules:
- Login broken after payment → Billing (NOT Technical)
- App crashes → Technical
- Pricing complaints + evaluating alternatives → Churn Risk
- Feature requests → Feature Request

Think step by step before classifying.

{format_instruction}'''),
     ('human', 'Subject: {subject}\nBody: {body}')
]).partial(format_instruction= parser.get_format_instructions())

chain = cot_prompt | llm | parser


# step : Loading the data
import json
import pandas 


with open('test_emails.json') as f:
    emails = json.load(f)


# lets prepare only for 20 emails

data={
 'id':[email['id'] for email in emails[:20]],
 'body':[email['body'] for email in emails[:20]],
 'category':[],
 'confidence':[],
 'reasoning' : []

}


# lets call the chain

output = chain.batch(emails[:20],config={"max_concurrency":10})

for i, email in enumerate(emails[:20]):
    data['category'].append(output[i].category)
    data['confidence'].append(output[i].confidence)
    data['reasoning'].append(output[i].resoning)


# lets save as csv file

df = pandas.DataFrame(data)

df.to_csv('classified_emails.csv',index=False)



