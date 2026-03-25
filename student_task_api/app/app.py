from fastapi import FastAPI
from app.routes import app

app = FastAPI(title="Student API")

app.include_router(app)