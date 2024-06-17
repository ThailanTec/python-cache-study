from redis import Redis

class RedisRepository:
    def __init__(self, redis_conn: Redis) -> None:
        self.__redis_con = redis_conn

    def insert(self, key: str, value: any) -> None:
        self.__redis_con.set(key, value)

    def get(self, key: str) -> any:
        value = self.__redis_con.get(key)
        if value:
            return value.decode("utf-8")

    def insert_hash(self, key: str, field:str, value: any) -> None:
        self.__redis_con.hset(key, field, value)

    def get_hash(self, key: str, filed: str) -> any:
        value = self.__redis_con.hget(key, filed)
        if value:
            return value.decode("utf-8")
    
    def insert_ex(self, key: str, value: any, ex: int) -> None:
        self.__redis_con.set(key, value, ex=ex)

    def insert_hash_ex(self, key: str, field:str, value: any, ex: int) -> None:
        self.__redis_con.hset(key, field, value)
        self.__redis_con.expire(key, ex)