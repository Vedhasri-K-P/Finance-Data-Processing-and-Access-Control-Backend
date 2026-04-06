import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI
from app.database import Base, engine

# Import models (VERY IMPORTANT)
from app.models import user, record  

# Import routers
from app.routes import user_routes, record_routes, dashboard_routes
from app.routes import auth_routes

# Create app FIRST
app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Include routers AFTER app is created
app.include_router(user_routes.router)
app.include_router(record_routes.router)
app.include_router(dashboard_routes.router)
app.include_router(auth_routes.router)

@app.get("/")
def root():
    return {"message": "Finance Backend Running"}