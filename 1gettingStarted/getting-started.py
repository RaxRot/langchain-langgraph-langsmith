import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

model_name=os.getenv("OPENAI_MODEL")
model = ChatOpenAI(model=model_name)

response = model.invoke("Where is the Statue of Liberty?")
print(response.content)