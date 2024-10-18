from pydantic import BaseModel
from datetime import datetime
from typing import Optional

from app.api.user.models import UserRole

class ResponseProfileSchema(BaseModel):
    fullname: str
    phone_number: str
    role: UserRole
    avatar_img: Optional[str] = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {  
                    
                    "fullname": "Иван Иванов",
                    "phone_number": "+79991234567",
                    "role": 'customer',
                    "avatar_img": "http://example.com/avatar.jpg"
                }
            ]
        }
    }

class ResponseUserSchema(BaseModel):
    id: int
    first_name: str
    second_name: str
    phone_number: str
    is_admin: bool
    is_superuser: bool
    is_active: bool

    model_config = {
        "json_schema_extra": {
            "examples": [
                {  
                    "id": 1,
                    "first_name": "Иван",
                    "second_name": "Иванов",
                    "phone_number": "+79991234567",
                    "is_admin": False,
                    "is_superuser": False,
                    "is_active": True
                }
            ]
        }
    }
