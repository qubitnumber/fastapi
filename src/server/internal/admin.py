from fastapi import APIRouter, Depends, Body
from fastapi.encoders import jsonable_encoder
from ..dependencies import get_internal_token


router = APIRouter(
    prefix="/admin",
    tags=["Admin"],
    dependencies=[Depends(get_internal_token)],
    responses={404: {"description": "Not found"}},
)
