from .connection import database
alphavantage_collection = database.get_collection("alphavantage")


# helpers
def alphavantage_helper(alphavantage) -> dict:
    return {
        "id": str(alphavantage["_id"]),
        "function": str(alphavantage["function"]),
        "symbol": str(alphavantage["symbol"]),
        "meta_data": alphavantage["meta_data"],
        "time_series": alphavantage["time_series"]
    }

from bson.objectid import ObjectId
# Retrieve all alphavantages present in the database
async def retrieve_alphavantages() -> list:
    alphavantages = []
    async for alphavantage in alphavantage_collection.find():
        alphavantages.append(alphavantage_helper(alphavantage))
    return alphavantages


# Add a new alphavantage into to the database
async def add_alphavantage(alphavantage_data: dict) -> dict:
    alphavantage = await alphavantage_collection.insert_one(alphavantage_data)
    new_alphavantage = await alphavantage_collection.find_one({"_id": alphavantage.inserted_id})
    return alphavantage_helper(new_alphavantage)


# Retrieve a alphavantage with a matching ID
async def retrieve_alphavantage_id(id: str) -> dict:
    alphavantage = await alphavantage_collection.find_one({"_id": ObjectId(id)})
    if alphavantage:
        return alphavantage_helper(alphavantage)


# Retrieve a alphavantage with a matching SYMBOL
async def retrieve_alphavantage_symbol(function: str, symbol: str) -> dict:
    query = {"function": function, "symbol": symbol}
    alphavantage = await alphavantage_collection.find_one(query)
    if alphavantage:
        return alphavantage_helper(alphavantage)


# Update a alphavantage with a matching ID
async def update_alphavantage_id(id: str, data: dict) -> bool:
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    alphavantage = await alphavantage_collection.find_one({"_id": ObjectId(id)})
    if alphavantage:
        updated_alphavantage = await alphavantage_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_alphavantage:
            return True
        return False

# Update a alphavantage with a matching SYMBOL
async def update_alphavantage_symbol(function: str, symbol: str, data: dict) -> bool:
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False

    updated_alphavantage = await alphavantage_collection.update_one(
        {"function": function, "symbol": symbol}, {"$set": data}, upsert=True
    )
    if updated_alphavantage:
        return True
    return False

# Delete a alphavantage from the database
async def delete_alphavantage(id: str) -> bool:
    alphavantage = await alphavantage_collection.find_one({"_id": ObjectId(id)})
    if alphavantage:
        await alphavantage_collection.delete_one({"_id": ObjectId(id)})
        return True