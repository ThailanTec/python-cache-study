import redis

redis_connection = redis.Redis(host="localhost", port=6379, db=0)


redis_connection.set("chave_1", "Relou Uourdi") 

valor = redis_connection.get("chave_1").decode("utf-8")
redis_connection.delete("chave_1")


redis_connection.hset("meu_rash", 'nome', 'thailan')
redis_connection.hset("meu_rash", 'idade', 'thailan')
redis_connection.hset("meu_rash", 'city', 'Bhz')
redis_connection.hdel("meu_rash", 'idade')

nome = redis_connection.hget('meu_nome', 'nome')
idade = redis_connection.hget('meu_nome', 'idade')
city = redis_connection.hget('meu_nome', 'city')

chave1 = redis_connection.exists("chave_1")
hash_key = redis_connection.exists("meu_rash")
field_key = redis_connection.hexists("meu_rash", "nome")
 