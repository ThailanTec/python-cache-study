import redis

class RedisRepository:
    def __init__(self, redis_conn: redis.Redis) -> None:
        self.__redis_conn = redis_conn

    def insert(self, key: str, value: any) -> None:
        self.__redis_conn.set(key, value)