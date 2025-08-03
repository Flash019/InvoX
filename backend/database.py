import os
from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
from pathlib import Path


# loading the .env
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME", "InvoX")  # fallback to InvoX

if not MONGO_URI:
    raise ValueError("MONGO_URI environment variable is not set")

# Sync client
client = MongoClient(MONGO_URI)
database = client[DB_NAME]
users_collection = database["DB"]  # this is the actual collection name
collection = users_collection  # <-- Export this to avoid ImportError

# Async client
async_client = AsyncIOMotorClient(MONGO_URI)
async_database = async_client[DB_NAME]
async_users_collection = async_database["DB"]

# Test connection
def test_connection():
    try:
        client.admin.command("ping")
        print(" Connected to MongoDB Atlas (sync)")
        return True
    except Exception as e:
        print(f" Sync MongoDB connection failed: {e}")
        return False

# Async test
async def test_async_connection():
    try:
        await async_client.admin.command("ping")
        print(" Connected to MongoDB Atlas (async)")
        return True
    except Exception as e:
        print(f" Async MongoDB connection failed: {e}")
        return False
