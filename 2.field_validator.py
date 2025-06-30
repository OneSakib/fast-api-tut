from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):
    name:  Annotated[str, Field(max_length=50, title="Name of the parient",
                                description="Give name of the parien of which is registed in hospital", examples=['Nitish', 'Amit'])]
    email: Annotated[EmailStr, Field(max_length=100)]
    linkedin_url: Annotated[AnyUrl, Field(max_length=50)]
    age: Annotated[int, Field(gt=1, lt=18)]
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(title='It should be bool')]
    allergies: Annotated[Optional[List[str]],
                         Field(default=None, max_length=5)]
    contact_details: Annotated[Dict[str, str],
                               Field(title="It should be Dict")]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domain = ['hdfc.com', 'icici.com']
        domain = value.split('@')[-1]
        if domain not in valid_domain:
            raise ValueError("Not a valid Domain")
        return value

    @field_validator('name', mode='after')
    @classmethod
    def transfer_name(cls, value):
        return value.upper()

    @field_validator('age', mode='after')
    @classmethod
    def age_check(cls, value):
        if value < 0 or value > 18:
            raise ValueError('Value should be greater then 0 or less than 18')
        return value


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
