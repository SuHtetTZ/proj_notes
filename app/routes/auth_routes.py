# routes/auth_routes.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies.auth import get_current_user
from app.service import auth_service
from app.schemas.user import UserCreate
from app.core.database import get_db

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    return auth_service.register(user, db)

@router.post("/login")
def login_user(email: str, password: str, db: Session = Depends(get_db)):
    return auth_service.login(email, password, db)

@router.get("/me")
def get_me(current_user = Depends(get_current_user)):
    return current_user
