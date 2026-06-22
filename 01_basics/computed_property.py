from pydantic import BaseModel, Field,computed_field

class Product(BaseModel):
    price: float
    quantity:int

    @computed_field   #calculate on the go
    @property         #make as accessible like attribute
    def total_price(self) -> float:
        return self.price * self.quantity
    
class Booking(BaseModel):
    user_id: int 
    room_id : int 
    nights: int = Field(...,ge=1)

    rate_per_night : float 
    @computed_field
    @property
    def total_amount(self) -> float:
        return self.nights * self.rate_per_night
    
booking = Booking(
    user_id = 123,
    room_id = 456,
    nights = 3,
    rate_per_night= 100.0
)
print(booking.total_amount)
print(booking.model_dump) # Badho Data print thai jse MODEL no 
    
