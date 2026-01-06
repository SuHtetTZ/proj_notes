from fastapi import FastAPI
from app.core.database import Base, engine
from app.models import user  # import models
from app.routes.auth_routes import router as auth_router
from app.routes.user_routes import router as user_router

app = FastAPI(title="MyApp")

# Dev only: drop & create
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(auth_router, prefix="/auth")
app.include_router(user_router, prefix="/users")
