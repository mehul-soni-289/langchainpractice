from langchain_openai import OpenAIEmbeddings 
from dotenv import load_dotenv
load_dotenv()

from sklearn.metrics.pairwise import cosine_similarity  
import numpy as np 

embedding = OpenAIEmbeddings(model="text-embedding-3-small"  , dimensions=300)
documents = [
    'Virat kohli is grea batsman' , 
    'Jasprit bumrah is the most proficient fast bowler' , 
    'hardik pandya is a good all rounder' ,
]

query = "tell me about virat kohli"  

documents_embeddings = embedding.embed_documents(documents) 
query_embedding = embedding.embed_query(query)


similarity_scores = cosine_similarity([query_embedding] , documents_embeddings)[0]


index , score = sorted(list(enumerate(similarity_scores))  , key = lambda x : x[1] , reverse=True)[0]

print(f"{index}  is the most similar document with similarity score of {score}")
