from pydantic import BaseModel ,EmailStr, AnyUrl,Field ,field_validator
from typing import List, Dict, Optional,Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, title='Name of patient', description='Enter name of patient in less than 50 characters', examples=['Rafia', 'Sawera']) ]
    email: EmailStr
    age: int
    weight: Annotated[float, Field(gt=0,strict =True)]
    married: Annotated[bool ,Field(default=None, description='Is the patient married or not ')]
    allergies: Optional[List[str]] = Field(max_length=5)
    contact_details: Dict[str,str] 
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains=['hdfc.com']
        domain_name=value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError('not a valid domain')
        return value


patient_info ={"name": "Rafia", "age": "20", "weight":45.1, "married":True, "allergies":['poller', 'dust']," contact_details":{'emial': 'abc@gmail.com',
'phone': '12345678980'}}
patient1= Patient(**patient_info)

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("inserted")

insert_patient_data(patient1)