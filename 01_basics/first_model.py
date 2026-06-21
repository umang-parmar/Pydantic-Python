from pydantic import BaseModel

class User(BaseModel):
    id:int
    name:str
    is_active:bool

input_data = {"id":101,"name":"Umang","is_active":True}

user = User(**input_data)
# ** is expand-unpack the dictionary(inside value scatered around treat Not only one object)
print(user)