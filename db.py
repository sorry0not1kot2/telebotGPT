from motor.motor_asyncio import AsyncIOMotorClient
import os

client = AsyncIOMotorClient(os.getenv('MONGO_URI'))

async def connect():
    await client.admin.command('ping')
    print('Connected to database')
