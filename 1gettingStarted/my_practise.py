from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os
load_dotenv()

model_name = os.getenv("OPENAI_MODEL")
model = ChatOpenAI(model=model_name)

request = input("Ask me: ")

response = model.invoke(request)
print(response.content)
