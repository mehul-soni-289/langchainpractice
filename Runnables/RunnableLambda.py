# By this runnable you can create any python function as runnable 


from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace 
from langchain_core.runnables import RunnableLambda , RunnableParallel , RunnablePassthrough
from dotenv import load_dotenv 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = HuggingFaceEndpoint (
    repo_id='meta-llama/Meta-Llama-3-8B-Instruct' , 
    task = 'text-generation'
)

model = ChatHuggingFace(llm=llm)

prompt1 = PromptTemplate(template = 'just generate me a joke on the topic of {topic}' , input_variables=['topic']) 

parser = StrOutputParser() 

sequence = prompt1 | model | parser 

def count_words(joke) : 
    return len(joke.split())


runnable_word_counter = RunnableLambda(count_words) 

parrallel_chain = RunnableParallel({
    'joke' : RunnablePassthrough() , 
    'word_count' : RunnableLambda(count_words)
})

final_chain = sequence | parrallel_chain

print(final_chain.invoke({'topic' : 'AI'}))