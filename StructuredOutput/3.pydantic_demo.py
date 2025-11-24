from pydantic import BaseModel , EmailStr , Field
from typing import Optional

class Student(BaseModel) : 
    name : str = 'mehul'
    surname : str
    age : Optional[int] = None
    # email : EmailStr
    # cgpa : float =  Field(gt =0 , lt=10 , description='hello')


new_student  = {'name' : 'nitish' , 'surname' : 'soni'}

student = Student(**new_student)

print(dict(student))