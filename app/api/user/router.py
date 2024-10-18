from typing import Annotated, List, Dict
from fastapi import APIRouter, Depends
import datetime

from app.api.user.schemas import ResponseProfileSchema
from app.api.user.models import User

router = APIRouter()


