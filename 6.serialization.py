from pydantic import BaseModel, EmailStr, AnyUrl, computed_field
from typing import List, Dict, Optional, Literal


class Address(BaseModel):
    city: str
    state: str
    zip_code: str


class Patient(BaseModel):
    name:  str
    email: EmailStr
    linkedin_url: AnyUrl
    age: int
    gender: str = "Male"
    weight: float
    height: float
    married: bool
    allergies: Optional[List[str]]
    contact_details: Dict[str, str]
    address: Address


data = {
    "name": "Sakib Malik",
    "email": 'abc@hdfc.com',
    "linkedin_url": 'https://linkdelin.com/w432dsfd',
    "age": 65,
    "weight": 30.5,
    "height": 1.72,
    "married": 0,
    "allergies": ['banana', 'banana', 'banana'],
    'contact_details': {'phone_number': '56546565656', 'email': 'abc@gmail.com', 'emergency': '5665656565'},
    'address': {
        'city': "Mohali",
        "state": "Punjab",
        "zip_code": '160071'
    }
}
patient = Patient(**data)
# print(patient.model_dump())
# print(patient.model_dump(include={'name'}))
# print(patient.model_dump(exclude={'name'}))
# print(patient.model_dump(exclude={'name'}))
print(patient.model_dump(exclude_unset=True))
# print(patient.model_dump_json())
