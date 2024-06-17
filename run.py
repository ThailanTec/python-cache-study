from models.redis.connection.connection import RedisConnectionHandle
from models.redis_repository import RedisRepository
from datetime import datetime
from config.start_form import start_form

# 1. Conectar no banco e buscar elementos
redis_conn = RedisConnectionHandle().connect()
redis_repo = RedisRepository(redis_conn)

data_actual = datetime.now()
data_formt = data_actual.strftime("%Y-%m-%d")
hash_itens = redis_conn.hgetall(data_formt)

# 2. Carregar dados ao formulario
my_dict = {}

for key, value in hash_itens.items():
    my_dict[key.decode("utf-8")] = value.decode('utf-8')


start_form.load_info(my_dict)

# 3. Utilizar valor armazenado
valor = start_form.get_info('banana')
print("Meu valor", valor)