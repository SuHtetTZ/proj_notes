# repositories/user_repo.py
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from datetime import datetime

# ----------------------------
# CRUD operations for User
# ----------------------------

def get_by_id(db: Session, user_id: int) -> User | None:
    return db.query(User).filter(User.id == user_id, User.deleted_at.is_(None)).first()


def get_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.email == email, User.deleted_at.is_(None)).first()


def get_all(db: Session) -> list[User]:
    return db.query(User).filter(User.deleted_at.is_(None)).all()


def create(db: Session, user_data: UserCreate) -> User:
    """
    user_data: UserCreate schema instance
    """
    new_user = User(
        name=user_data.name,
        email=user_data.email,
        phone=user_data.phone,
        dob=user_data.dob,
        address=user_data.address,
        password=user_data.password,  # already hashed by service
        role=user_data.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def soft_delete(db: Session, user_id: int) -> None:
    """
    Marks deleted_at instead of removing
    """
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.deleted_at = datetime.utcnow()
        db.commit()
