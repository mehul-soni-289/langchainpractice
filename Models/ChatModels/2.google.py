from langchain_google_genai import ChatGoogleGenAI
from dotenv import load_dotenv  
load_dotenv()

model = ChatGoogleGenAI(model='gemini-pro', temperature=0.7)

result = model.invoke('What is the capital of India?')
print(result.content)