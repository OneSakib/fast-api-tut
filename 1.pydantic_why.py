from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):
    name:  str
    email: EmailStr
    linkedin_url: AnyUrl
    age: int
    weight: float
    married: bool
    allergies: Optional[List[str]]
    contact_details: Dict[str, str]


data = {
    "name": "Sakib Malik",
    "email": 'abc@hdfc.com',
    "linkedin_url": 'https://linkdelin.com/w432dsfd',
    "age": '17',
    "weight": 30.5,
    "married": 0,
    "allergies": ['banana', 'banana', 'banana'],
    'contact_details': {'phone_number': '56546565656', 'email': 'abc@gmail.com'}
}
patient = Patient(**data)
print(patient)
