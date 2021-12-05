import os

from dotenv import load_dotenv

load_dotenv(verbose=True)

from pymongo import MongoClient

mongo_client = MongoClient(
    host=os.getenv('MONGO_HOST_', '127.0.0.1'),
    port=int(os.getenv('MONGO_PORT_', 27017)),
    username=os.getenv('MONGO_USER_', None),
    password=os.getenv('MONGO_PASS_', None),
    maxPoolSize=int(os.getenv('MAX_P', 90)),
    waitQueueTimeoutMS=int(os.getenv('TIMEOUT_MS', 10000))
)
