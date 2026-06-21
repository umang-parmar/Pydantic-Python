from pydantic import BaseModel
from typing import List , Dict , Optional

class Cart(BaseModel):
    user_id:int
#from pydantic borrowed str & from typing borrowed List 
    items: List[str] #List only containing string
    quantities:Dict[str,int] #keys=string, values=integer

class BlogPost(BaseModel):
    title: str
    content : str
    image_url : Optional[str] = None #string or None 