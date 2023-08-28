from fastapi import FastAPI, HTTPException
from model import User, Gender, Role, UpdateUser
from typing import List
from uuid import uuid4, UUID


app = FastAPI()

db: List[User] = [
    User(id=UUID('0b0d6f94-1240-4bd1-889d-302b95656e75'), first_name='John', last_name='testing', middlename='', gender=Gender.Male, role=[Role.Admin, Role.User]),
    User(id=UUID('00ba28d2-bfb6-4248-b3ca-c9c7f6c8d108'), first_name='Mary', last_name='testing', middlename='pydantic', gender=Gender.Female, role=[Role.User]),
    User(id=UUID('feb40e09-c3d1-4bd8-b825-6a72106fe5f6'), first_name='Jamila', last_name='Ibrahim', middlename='', gender=Gender.Male, role=[Role.Student]),
]

@app.get('/')
def root():
    return {'message': 'Hello World'} 

@app.get('/api/v1/users')
async def fetch_users():
    return db

@app.post('/api/v1/users')
async def add_user(user: User):
    db.append(user)
    return {'id': user.id}

@app.put('/api/v1/users/{id}')
async def update_user(update: UpdateUser, id: UUID):
    for user in db:
        if user.id == id:
            if update.first_name is not None:
                user.first_name = update.first_name
            if update.last_name is not None:
                user.last_name = update.last_name
            if update.middlename is not None:
                user.middlename = update.middlename
            if update.gender is not None:
                user.gender = update.gender
            if update.role is not None:
                user.role = update.role
            return {'message': 'User updated successfully'}
    raise HTTPException(
        status_code=404,
        detail=f'User with id: {user.id} not found',
    )

@app.delete('/api/v1/users/{id}')
async def delete_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return {'message': 'User deleted successfully'}
    raise HTTPException(
        status_code=404,
        detail=f'User with id: {user.id} not found',
    )