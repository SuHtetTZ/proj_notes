from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date, datetime
from enum import IntEnum

class UserRole(IntEnum):
    ADMIN = 0
    USER = 1

class UserBase(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str]
    dob: Optional[date]
    address: Optional[str]
    role: UserRole = UserRole.USER

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    