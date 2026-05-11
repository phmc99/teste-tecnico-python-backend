from fastapi import FastAPI
from app.routes.registros import router

app = FastAPI()

app.include_router(router)