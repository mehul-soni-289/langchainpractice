from langchain_openai import ChatOpenAI 
from dotenv import load_dotenv 
from typing import TypedDict , Annotated , Optional , Literal
from pydantic import Field , BaseModel

load_dotenv() 


model = ChatOpenAI() 

# class Review(TypedDict) : 
    # key_themes : Annotated[list[str]  , 'write down all the key theme discussed in review']
    # summary: Annotated[str,'A brief summary of review'] 
    # sentiment : Annotated[Literal['pos' , 'neg'] , 'Return sentimate of the review']
    # pros  : Annotated[Optional[list[str]] , 'list down all the pros']


class Review(BaseModel) : 
    key_themes : list[str] = Field(description='write down all the')
    summary : str = Field(description="A brief summary of the review")
    sentiment : Literal['pos' , 'neg'] = Field(description='return sentiment of the review ')
    pros : Optional[list[str]] = Field(default = None  , description='write down all the pros')



structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""
The hardware is great , but the software feels bloated . There are too many  pre-installed apps 
""")
print(result)
