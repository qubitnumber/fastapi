from fastapi import Header, HTTPException
from decouple import config
EXTERNAL_TOKEN = config("EXTERNAL_TOKEN")
INTERNAL_TOKEN = config("INTERNAL_TOKEN")

async def get_external_token(x_token: str = Header()):
    if x_token != EXTERNAL_TOKEN:
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def get_internal_token(i_token: str):
    if i_token != INTERNAL_TOKEN:
        raise HTTPException(status_code=400, detail="No Jessica token provided")