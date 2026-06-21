from pydantic import BaseModel

class Product(BaseModel):
    id:int
    name:str
    price:float
    in_stock:bool = True

product_one = Product(id=1,name="Laptop",price=99.99,in_stock=True)
product_two = Product(id=2,name="Mouse",price=23.99)

#Always use type annotation(int,float,str,bool etc...) :Set Sensible default
# "123" -> 123 
# "True" -> True 
# 123 => 123.0 