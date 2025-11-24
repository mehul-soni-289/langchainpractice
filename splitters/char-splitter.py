from langchain.text_splitter import CharacterTextSplitter 
from langchain_community.document_loaders import PyPDFLoader 


loader = PyPDFLoader("dl-curriculum.pdf") 

documents = loader.load() 

text_splitter = CharacterTextSplitter(

 chunk_size = 100 , 
 chunk_overlap = 0  , 
 separator=''

)

splited_documents = text_splitter.split_documents(documents)
# splited_text = text_splitter.split_text('texthere')
print(len(splited_documents))