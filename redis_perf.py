from models.redis.connection.connection import RedisConnectionHandle
from models.redis_repository import RedisRepository
from models.sql.mysql_repository import MysqlRepository

redis_conn = RedisConnectionHandle().connect()
redis_repo = RedisRepository(redis_conn)
mysql_repo = MysqlRepository()

name = "Minevaldo"

# Logica de busca

value = redis_repo.get(name)

print("buscando Redis")
if value:
    print('Achei no redis!!')
    print("Valor redis",value)
else:
    print("Buscando no Mysql")
    value_2 = mysql_repo.select_by_name(name)
    print("Achei no Mysql!")
    redis_repo.insert_ex(name, value_2,10)

