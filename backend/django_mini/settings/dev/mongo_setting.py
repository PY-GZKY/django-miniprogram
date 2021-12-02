import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(verbose=True)

from pymongo import MongoClient

mongo_client = MongoClient(
    host=os.getenv('MONGO_HOST', '127.0.0.1'),
    port=int(os.getenv('MONGO_PORT', 27017)),
    username=os.getenv('MONGO_USER', None),
    password=os.getenv('MONGO_PASS', None),
    maxPoolSize=int(os.getenv('MAX_P', 90)),
    waitQueueTimeoutMS=int(os.getenv('TIMEOUT_MS', 10000))
)

