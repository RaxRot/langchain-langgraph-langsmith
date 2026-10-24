from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model="gpt-6-luna")

request = input("Ask me: ")

response = model.invoke(request)
print(response.content)
