from models.connection.connection import RedisConnectionHandle
from models.redis_repository import RedisRepository

redis_conn = RedisConnectionHandle().connect()

redis_repo = RedisRepository(redis_conn)

redis_repo.insert("aula", '2')
redis_repo.insert("a","s")
