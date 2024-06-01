from redis import Redis

class RedisRepository:
    def __init__(self, redis_conn: Redis) -> None:
        self.__redis_con = redis_conn

    def insert(self, key: str, value: any) -> None:
        self.__redis_con.set(key, value)
        