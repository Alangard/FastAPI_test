from typing import List, Dict
from fastapi import APIRouter, Depends
import datetime
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_async_session
from app.api.appointments.schemas import ResponseAppointmentSchema, RequestAppointmentSchema

router = APIRouter()

@router.get("/appointments/", response_model=List[ResponseAppointmentSchema])
async def get_appointments(
        skip: int = 0, 
        limit: int = 15, 
        date_from: datetime.datetime = None, 
        date_to: datetime.datetime = None,
        executor_id: int = None,
        customer_id: int = None,
        session: AsyncSession = Depends(get_async_session) #to do: check is admin or any with 'executor' role
    ):
    return None

@router.get("/appointments/{appointment_id}/", response_model=ResponseAppointmentSchema)
async def get_appointment(appointment_id: int, session: AsyncSession = Depends(get_async_session)):
    return None

@router.post("/appointments", response_model=ResponseAppointmentSchema)
async def create_appointment(user_data: RequestAppointmentSchema, session: AsyncSession = Depends(get_async_session)):
    return None

@router.patch("/appointments/{appointment_id}", response_model=ResponseAppointmentSchema)
async def update_appointment(user_data: Dict, session: AsyncSession = Depends(get_async_session)):
    return None

@router.delete("/appointments/{appointment_id}/")
async def delete_user(user_id: int):
    return None

