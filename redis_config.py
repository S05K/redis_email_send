import os
from dotenv import load_dotenv
import redis

load_dotenv()

class RedisConfig:
    REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT = int(os.getenv("REDIS_PORT", 6379)) 
    REDIS_DB = int(os.getenv("REDIS_DB", 0)) 

    @classmethod
    def create_redis_client(cls):
        client = redis.Redis(host=cls.REDIS_HOST, port=cls.REDIS_PORT, db=cls.REDIS_DB)
        return client
