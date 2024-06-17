Site do Redis:
https://redis.io/

### O que é o Redis?

Datastorage de código aberto, rápido e na memória e para uso como banco de dados, cache, agente de mensagens e fila.

### Como funciona o armazenamento no Redis?

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/ea9dccf6-7ab8-443c-bff2-9d4deaf3ce72/5b74b038-caac-4b72-b90b-a466f3c5612e/Untitled.png)

No Redis, trabalhamos com chave-valor, onde, para cada chave vamos ter um valor associado ao mesmo. Também, podemos ter chaves hash, onde essas chaves vão ter varios campos tipo um dicionario de python. 

Podemos utilizar o programa:

https://goanother.com/

Assim, conseguimos de forma visual, verificar quais são os dados que estão sendo armazenados dentro do cache redis. 

### Comandos Redis com Python

Com o pip, podemos instalar a lib do redis:

```python
pip install redis
```

Para conectar a nossa aplicação a um banco Redis, precisamos apenas do seguinte comando:

```python

import redis

redis_connection = redis.Redis(host="localhost", port=6379, db=0)

```

Agora, para setar um valor dentro do redis, podemos salvar da seguinte da seguinte forma:

```python

redis_connection.set("chave_1", "Relou Uourdi") 

```

Assim, já conseguimos deixar salvo dentro do banco tais informações. 

Para recuperar, podemos utilizar o seguinte comando:

```python

valor = redis_connection.get("chave_1").decode("utf-8")

print(valor)

```

Assim, sendo realmente simples de cadastrar um chave no banco e de recuperar. 

***Obs*: Nota-se que na linha da váriavel valor, temos um comando extra sendo passado:** 

*decode***, esse comando é necessario pois o retorno do redis é em bytes e precisamos do mesmo em string ou do seu valor armazenado em banco.** 

### Trabalhando com Hash

Para criar um Hash(dicionario), podemos fazer da seguinte forma:

```python
redis_connection.hset("meu_rash", 'nome', 'thailan')
redis_connection.hset("meu_rash", 'idade', 'thailan')
redis_connection.hset("meu_rash", 'city', 'Bhz')
```

Steps:

1 - Criar o nome do rash

2- Informar o nome do campo (chave)

3- Informar o valor do campo (valor)

Para recuperar é um pouco diferente. Passamos um ‘h’, na frente do get. Ficando então, da seguinte forma a maneira de recuperar os dados de dentro do hash:

```python
nome = redis_connection.hget('meu_nome', 'nome').decode("utf-8")
idade = redis_connection.hget('meu_nome', 'idade').decode("utf-8")
city = redis_connection.hget('meu_nome', 'city').decode("utf-8")

print(nome, idade, city)
```

Assim, temos a base de armazenamento e recuperação de dados no redis. 

**Deletar dados do Redis**

Para deletar dados podemos passar os seguintes comandos:

Deletar Chave-Valor:

```python

redis_connection.delete("chave_1")

```

Deletar Hash:

```python
redis_connection.hdel("meu_rash", 'idade')
```

A diferença é que para deletar um hash, passamos apenas o comando *hdel* ao invez de escrever *delete* por completo.

**Checando se as chaves existem**

Para verificar se as chaves existem, podemos utilizar os seguintes comandos:

```python
chave1 = redis_connection.exists("chave_1")
hash_key = redis_connection.exists("meu_rash")
field_key = redis_connection.hexists("meu_rash", "nome")
```

1. Verificando se a chave existe
2. Verificando se o hash existe
3. Verificando se a chave ‘nome’ existe dentro do hash: ‘meu_rash’

São essas três formas de verificar a existencia do dados. Assim, deixando mais fácil de verificar para criar ou dado um motivo em especifico. 

O código do repositorio nosso é:
https://github.com/ThailanTec/python-cache-study/

### Entendendo o TTL do Redis (Time to live)

É um valor inteiro que especifica o número de segundos até que a chave expire. O Redis pode especificar segundos ou milissegundos para esse valor. 

Com ele, conseguimos deixar dados guardados no nosso código, para que assim a gente consiga recuperar as informações de forma mais rápida que no sql, pois ele é mais performatico. 

Como por exemplo:

Código do repositorio:

```python
    def insert_ex(self, key: str, value: any, ex: int) -> None:
        self.__redis_con.set(key, value, ex=ex)

    def insert_hash_ex(self, key: str, field:str, value: any, ex: int) -> None:
        self.__redis_con.hset(key, field, value)
        self.__redis_con.expire(key, ex)
        
```

Código de chamada de criação dos dados:

```python

redis_repo.insert_hash_ex(data_formt, "banana", 3.21, 30)
redis_repo.insert_hash(data_formt, "Uva", 4.13)
redis_repo.insert_hash(data_formt, "Pistache", 8.21)
```

Assim, os dados são excluidos de forma automatica com o tempo passado inicialmente.

### Adicionando Performance ao Redis com váriavel

Trabalhando com redis, podemos intrudozir o seu resultado em váriaveis, assim deixando em nossa mémoria de código o resultado das nossas buscas, deixando então, mais fácil a busca e economizando recursos de uma forma “elegante” para a aplicação.

Então, podemos fazer um Singleton, para facilitar na recuperação das informações. 
**Exemplo:**

```python
from typing import Dict

class __StartForm:
    def __init__(self) -> None:
        self.__cache_data = None
    
    def load_info(self, data: Dict ) -> None:
        self.__cache_data = data
    
    def get_info(self, key: str) -> str:
        if key in self.__cache_data:
            return self.__cache_data[key]
        return None
    

start_form = __StartForm()

```

Assim, podemos utilizar a váriavel start_form em outros locais do código e usar ela e o load_info para recuperar e armazenar as informações dentro da função. 

### Performance Redis com banco de dados

Trabalhando com o banco de dados Redis, colocamos ele na frente no banco de dados para fazer as consultas, pois como o mesmo tem uma maior velocidade de retorno dos dados o mesmo vem com uma performance fora da curva. 

No exemplo do nosso repo, criamos o que séria a estrutura de banco de dados, onde nela temos um “get” fake para fazer a requisição. Se não localizar ele salva no redis e depois devolve os dados para as proximas consultas. Segue o código de exemplo:

```python
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

```

Adicionamos ainda um timming, pois depois de certo tempo o dado vai ser deletado e aplicação vai conseguir puxar as informações desse banco de dados.