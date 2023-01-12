from fastapi import APIRouter, Depends, Body
from fastapi.encoders import jsonable_encoder
from ..dbs.alphavantage import (
    add_alphavantage,
    delete_alphavantage,
    retrieve_alphavantage_id,
    retrieve_alphavantage_symbol,
    retrieve_alphavantages,
    update_alphavantage_id,
    update_alphavantage_symbol,
)
from ..models.alphavantage import (
    ErrorResponseModel,
    ResponseModel,
    AlphavantageSchema,
    UpdateAlphavantageModel,
)
from ..dependencies import get_internal_token


router = APIRouter(
    prefix="/alphavantage",
    tags=["Alphavantage"],
    dependencies=[Depends(get_internal_token)],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_description="Alphavantage data added into the database")
async def add_alphavantage_data(alphavantage: AlphavantageSchema = Body(...)):
    alphavantage = jsonable_encoder(alphavantage)
    new_alphavantage = await add_alphavantage(alphavantage)
    return ResponseModel(new_alphavantage, "Alphavantage added successfully.")

@router.get("/", response_description="Alphavantages retrieved")
async def get_alphavantages():
    alphavantages = await retrieve_alphavantages()
    if alphavantages:
        return ResponseModel(alphavantages, "Alphavantages data retrieved successfully")
    return ResponseModel(alphavantages, "Empty list returned")

@router.get("/{id}", response_description="Alphavantage data retrieved by ID")
async def get_alphavantage_data_id(id: str):
    alphavantage = await retrieve_alphavantage_id(id)
    if alphavantage:
        return ResponseModel(alphavantage, "Alphavantage data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Alphavantage doesn't exist.")

@router.get("/{function}/{symbol}", response_description="Alphavantage data retrieved by SYMBOL")
async def get_alphavantage_data_symbol(function: str, symbol: str):
    alphavantage = await retrieve_alphavantage_symbol(function, symbol)
    if alphavantage:
        return ResponseModel(alphavantage, "Alphavantage data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Alphavantage doesn't exist.")

@router.put("/{id}")
async def update_alphavantage_data_id(id: str, req: UpdateAlphavantageModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_alphavantage = await update_alphavantage_id(id, req)
    if updated_alphavantage:
        return ResponseModel(
            "Alphavantage with ID: {} name update is successful".format(id),
            "Alphavantage name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        403,
        "There was an error updating the alphavantage data.",
    )

@router.put("/{function}/{symbol}")
async def update_alphavantage_data_symbol(function: str, symbol: str, req: UpdateAlphavantageModel = Body(...)):
    updated_alphavantage = await update_alphavantage_symbol(function, symbol, req)
    if updated_alphavantage:
        return ResponseModel(
            "Alphavantage with SYMBOL: {} name update is successful".format(symbol),
            "Alphavantage name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        403,
        "There was an error updating the alphavantage data.",
    )

@router.delete("/{id}", response_description="Alphavantage data deleted from the database")
async def delete_alphavantage_data(id: str):
    deleted_alphavantage = await delete_alphavantage(id)
    if deleted_alphavantage:
        return ResponseModel(
            "Alphavantage with ID: {} removed".format(id), "Alphavantage deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Alphavantage with id {0} doesn't exist".format(id)
    )