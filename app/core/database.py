from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    echo=True  #to print SQL in console
)
Base = declarative_base()   # blueprint maker, so that sqlalchemy knows it's a tabel
# Session factory for each db session
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)

def get_db():
    """
    Yield a database session, then close it after request.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
