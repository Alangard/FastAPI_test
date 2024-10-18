
from datetime import datetime
from typing import Any, List, Optional
from enum import Enum as PyEnum
from sqlalchemy import Boolean, DateTime, Enum, Float,  ForeignKey,Integer, String, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import TIMESTAMP
from app.database import BaseModel


class UserRole(PyEnum):
    customer = "customer"
    executor = "executor"

class User(BaseModel):
    __tablename__= "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    first_name: Mapped[str] = mapped_column(String(50))
    second_name: Mapped[str] = mapped_column(String(50))
    phone_number: Mapped[str] = mapped_column(String, unique=True)
    password: Mapped[str] = mapped_column(String)
    is_admin: Mapped[bool] = mapped_column(default=False, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(default=False, nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True, nullable=False)

    user_profile: Mapped['UserProfile'] = relationship("UserProfile", back_populates="user", uselist=False)

    def fullname(self):
        return (self.first_name + self.second_name).title()

class UserProfile(BaseModel):
    __tablename__= "profiles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    birthdate: Mapped[Optional[datetime]] 
    role: Mapped[UserRole] = mapped_column(Enum(UserRole), default="customer")
    avatar_img: Mapped[Optional[str]]
    
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))
    user: Mapped["User"] = relationship("User", back_populates="user_profile")