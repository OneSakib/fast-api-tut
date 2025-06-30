from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):
    name:  Annotated[str, Field(max_length=50, title="Name of the parient",
                                description="Give name of the parien of which is registed in hospital", examples=['Nitish', 'Amit'])]
    email: Annotated[EmailStr, Field(max_length=100)]
    linkedin_url: Annotated[AnyUrl, Field(max_length=50)]
    age: Annotated[int, Field(title="Age ")]
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(title='It should be bool')]
    allergies: Annotated[Optional[List[str]],
                         Field(default=None, max_length=5)]
    contact_details: Annotated[Dict[str, str],
                               Field(title="It should be Dict")]

    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError(
                "Patient holder must age 60 and emerygency contact number")
        return model


data = {
    "name": "Sakib Malik",
    "email": 'abc@hdfc.com',
    "linkedin_url": 'https://linkdelin.com/w432dsfd',
    "age": 65,
    "weight": 30.5,
    "married": 0,
    "allergies": ['banana', 'banana', 'banana'],
    'contact_details': {'phone_number': '56546565656', 'email': 'abc@gmail.com', 'emergency': '5665656565'}
}
patient = Patient(**data)
print(patient)
