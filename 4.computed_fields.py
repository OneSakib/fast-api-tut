from pydantic import BaseModel, EmailStr, AnyUrl, computed_field
from typing import List, Dict, Optional


class Patient(BaseModel):
    name:  str
    email: EmailStr
    linkedin_url: AnyUrl
    age: int
    weight: float
    height: float
    married: bool
    allergies: Optional[List[str]]
    contact_details: Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        value = round(self.age*(self.height**2), 2)
        return value


data = {
    "name": "Sakib Malik",
    "email": 'abc@hdfc.com',
    "linkedin_url": 'https://linkdelin.com/w432dsfd',
    "age": 65,
    "weight": 30.5,
    "height": 1.72,
    "married": 0,
    "allergies": ['banana', 'banana', 'banana'],
    'contact_details': {'phone_number': '56546565656', 'email': 'abc@gmail.com', 'emergency': '5665656565'}
}
patient = Patient(**data)
print(patient)
