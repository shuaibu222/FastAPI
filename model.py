from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID, uuid4
from enum import Enum

class Gender(str, Enum):
    Male = "Male"
    Female = "Female"

class Role(str, Enum):
    Admin = "Admin"
    User = "User"
    Student = "Student"

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    middlename: Optional[str]
    gender: Gender
    role: List[Role]

class UpdateUser(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    middlename: Optional[str]
    gender: Optional[Gender]
    role: Optional[List[Role]]