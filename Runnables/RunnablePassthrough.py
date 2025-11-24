
from langchain_huggingface import HuggingFaceEndpoint , ChatHuggingFace
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import StrOutputParser 
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableParallel, RunnablePassthrough
from langchain_openai import ChatOpenAI


load_dotenv()

llm = HuggingFaceEndpoint (
    repo_id='meta-llama/Meta-Llama-3-8B-Instruct' , 
    task = 'text-generation'
)

model = ChatHuggingFace(llm=llm)
# model = ChatOpenAI()

prompt1 = PromptTemplate(template='Generate me a joke on the topic of {topic}' , input_variables=['topic'])

prompt2 = PromptTemplate(template='Explain this joke in detail {joke}' , input_variables=['joke']) 

parser = StrOutputParser()
sequence_chain = prompt1 | model |parser 

p_chain = RunnableParallel(
    {
        'joke' : RunnablePassthrough() , 
        'explanation' : prompt2 | model | parser
    }
)

ans_chain=sequence_chain|p_chain

print(ans_chain.invoke({'topic' : 'computer'}))