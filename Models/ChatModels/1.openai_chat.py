from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


model = ChatOpenAI(model='gpt-4' , temperature=0.7)
# temprature controls the randomness of the output
# less temprature means more focused and deterministic output
# more temprature means more random and creative output

result = model.invoke('What is the capital of India?')


print(result.content)
