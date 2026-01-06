# services/auth_service.py
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repositories.user_repo import get_by_email, create_user
from app.core.security import verify_password, hash_password, create_access_token
from app.schemas.user import UserCreate

def register(user_data: UserCreate, db: Session):
    existing_user = get_by_email(db, user_data.email)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

    hashed_pw = hash_password(user_data.password)
    user_data.password = hashed_pw
    return create_user(db, user_data)

def login(email: str, password: str, db: Session):
    user = get_by_email(db, email)
    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    token_data = {"sub": user.id, "role": user.role.value}
    token = create_access_token(token_data)
    return {"access_token": token, "token_type": "bearer"}
