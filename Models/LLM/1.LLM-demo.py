# from langchain import OpenAI
# from dotenv import load_dotenv

# load_dotenv() 

# llm = OpenAI(model='gtp-3.5-turbo-instruct')

# llm.invoke("What is the capital of India?")


from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# Use ChatOpenAI for gpt-3.5-turbo
llm = ChatOpenAI(model="gpt-3.5-turbo")

result = llm.invoke("What is the capital of India?")

print(result.content)  # .content gives the text reply
