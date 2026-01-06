from fastapi import APIRouter, Depends
from app.models.user import User
from app.core.database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/users'
)

@router.get('/')
def all_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@router.get('/{id}')
def get_user(id: int):
    pass

@router.delete('/{id}')
def delete_user(id: int):
    pass