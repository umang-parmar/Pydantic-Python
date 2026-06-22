from pydantic import BaseModel,field_validator,model_validator

class User(BaseModel):
    username:str

    @field_validator('username')
    def username_length(cls,v):   # v: actual value to apply to thise validation ,cls:whole class is available
        if len(v) < 4:
            raise ValueError("username must be at least 4 character")
        return v
    
class SignupData(BaseModel):
    password: str
    confirm_password:str
    #after: Runs after the feild validation , values: its model validator it access all the values at same time
    @model_validator(mode='after') 
    def password_match(cls,v): 
        if v.password != v.confirm_password:
            raise ValueError("Password Do not match")
        return v