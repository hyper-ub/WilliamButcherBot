from motor.motor_asyncio import AsyncIOMotorClient
from ....sample_config import mongo_db_uri


client = AsyncIOMotorClient(mongo_db_uri)
db = client.wbb