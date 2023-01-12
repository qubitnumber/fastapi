from decouple import config
MONGO_DETAILS = config("MONGO_DETAILS")

import motor.motor_asyncio
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS, tls=True, tlsAllowInvalidCertificates=True)
database = client.qubitnumber