from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint 
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv 

load_dotenv() 

llm = HuggingFaceEndpoint (
    repo_id='meta-llama/Meta-Llama-3-8B-Instruct' , 
    task = 'text-generation'
)

model = ChatHuggingFace(llm=llm)

# 1st prompt -> detailed report 
template = PromptTemplate( 
    template='Write a detailed report on {topic}' , 
    input_variables=['topic']
)


template2 =  PromptTemplate(
    template='write 5 line summary on  the following    text \n {text}' , 
    input_variables=['text']
)


prompt1 = template.invoke({'topic' : 'black hole'})
result  = model.invoke(prompt1)

prompt2 = template2.invoke({'text' : result.content})

result1 = model.invoke(prompt2)

print(result1.content)