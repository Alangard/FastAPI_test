from pydantic import BaseModel
import datetime
from typing import Optional
from enum import Enum as PyEnum

from app.api.user.schemas import ResponseProfileSchema

class ServiceType(PyEnum):
    examination = "examination"
    tests = "tests"

class RequestAppointmentSchema(BaseModel):
    executor_id: int
    appointment_date: datetime.datetime
    service_type: ServiceType
    customer_description: Optional[str] = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {   
                    "executor_id": 1,
                    "appointment_date": datetime.datetime.now(datetime.timezone.utc),
                    "service_type": "examination" ,
                    "customer_description": "Хочу, чтобы сделали укол строго по координатам",
                }
            ]
        }
    }

class ResponseAppointmentSchema(BaseModel):

    executor: ResponseProfileSchema
    customer: ResponseProfileSchema
    appointment_date: datetime.datetime
    service_type: ServiceType
    customer_description: Optional[str] = None
    executor_description: Optional[str] = None
    
    created_on: datetime.datetime
    updated_on: datetime.datetime

    model_config = {
        "json_schema_extra": {
            "examples": [
                {   
                    "customer": {
                        "fullname": "Иван Иванов Иванович",
                        "phone_number": "+79991234567",
                        "role": 'customer',
                        "avatar_img": "http://example.com/avatar.jpg"
                    },
                    "executor": {
                        "fullname": "Петр Петров Васильевич",
                        "phone_number": "+79997654321",
                        "role": "executor",
                        "avatar_img": "http://example.com/avatar2.jpg"
                    },
                    "executor_description": "Надоедливый клиент",
                    "customer_description": "Хочу, чтобы сделали укол строго по координатам",
                    "service_type": "examination" ,
                    "created_on": datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=3),
                    "updated_on": datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=2),
                }
            ]
        }
    }















