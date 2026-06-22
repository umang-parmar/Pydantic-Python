from typing import Optional 
from pydantic import BaseModel,Field

class Employee(BaseModel):
    id:int
    name:str= Field(
        ...,                #This Field Is Required
        min_length=3,
        max_length=50,
        description="Employee Name",
        examples="Umang Parmar"
    )
    department:Optional[str]='General'
    salary:float=Field(
        ...,
        ge=10000
    )

class User(BaseModel):
    email:str=Field(..., pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    phone:str=Field(..., pattern=r"^[6-9]\d{9}$")
    age:int=Field(
        ...,
        ge=0,
        le=150,
        description="Age in years"
    )
    discount:float = Field(
        ...,
        ge=0,
        le=100
    )  

emp = Employee(
    id=1,
    name="Umang Parmar",
    department="IT",
    salary=50000
)
print(emp)

user = User(
    email="umang@gmail.com",
    phone="9876543210",
    age=25,
    discount=20
)
print(user)

# https://regexr.com/  JOI LEVU EK VAT AA WEBSITE DOCS TO VALIDATION:PHONE NO , EMAIL