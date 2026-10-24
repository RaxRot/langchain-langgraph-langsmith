from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model="gpt-6-luna")

response = model.invoke("Where is the Statue of Liberty?")
print(response.content)