from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import asyncio
from .routes import student
from .internal import admin, alphavantage
from .services.alphavantage.alphavantage import (
    update_daily,
    update_intraday
)

app = FastAPI()
origins = ['https://localhost:3000']
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)
app.include_router(student.router)
app.include_router(alphavantage.router)
app.include_router(admin.router)

@app.get("/", tags=["Root"])
async def read_root():
    await update_daily("TSLA")
    await update_intraday("TSLA")
    return {"message": "Welcome to this fantastic app!"}


















































































    

