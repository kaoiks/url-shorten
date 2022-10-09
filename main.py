from fastapi import FastAPI
from api import redirect_api

app = FastAPI()

app.include_router(redirect_api.router)

