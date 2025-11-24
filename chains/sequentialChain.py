# To do : we have to generte the detailed report on the topic and after that retrive the top 5 points of the topi 

from langchain_huggingface import HuggingFaceEndpoint , ChatHuggingFace
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import StrOutputParser 
from dotenv import load_dotenv


load_dotenv()

llm = HuggingFaceEndpoint (
  repo_id="google/gemma-2-2b-it",
    task = 'text-generation'
)


model = ChatHuggingFace(llm = llm)

prompt1 = PromptTemplate(
template='Generate me the detailed report for {topic}' , 
input_variables= ['topic']
)

prompt2 = PromptTemplate(
    template='give the most five important points for the given text \n {text}' , 
    input_variables=['text']
)

parser = StrOutputParser() 

chain = prompt1 | model | parser |prompt2 | model | parser 

result = chain.invoke({'topic' : 'cricket'})

print(result)
