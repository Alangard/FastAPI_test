from pydantic import BaseModel, Field, field_validator
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Form
import re

class UserRegister(BaseModel):
    first_name: str = Field(..., min_length=3, max_length=50)
    second_name: str = Field(..., min_length=3, max_length=50)
    phone_number: str
    password: str
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {  
                    "first_name": "Иван",
                    "second_name": "Иванов",
                    "phone_number": "+79991234567",
                    "password": 'ivanov978',
                }
            ]
        }
    }

    @field_validator("phone_number")
    @classmethod
    def validate_phone_number(cls, value: str) -> str:
        if not re.match(r'^\+\d{5,15}$', value):
            raise ValueError('Номер телефона должен начинаться с "+" и содержать от 5 до 15 цифр')
        return value
    
class UserAuth(BaseModel):
    phone_number: str
    password: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {  
                    "phone_number": "+79991234567",
                    "password": 'ivanov978',
                }
            ]
        }
    }

class Token(BaseModel):
    access_token: str
    token_type: str
    refresh_token: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {  
                    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIrNzk5OTEyMzQ1NjciLCJleHAiOjE3MjkyNDQzMjZ9.yGUBdNZRoXLljarN4rjsrs_9iBXgiwnU9EHN4vMCeKA",
                    "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIrNzk5OTEyMzQ1NjciLCJleHAiOjE3MjkyNDQzMjZ9.yGUBdNZRoXLljarN4rjsrs_9iBXgiwnU9EHN4vMCeXE",
                    "token_type": "bearer"
                }
            ]
        }
    }



