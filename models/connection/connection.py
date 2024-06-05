from .options_connection import options_connection
from redis import Redis

class RedisConnectionHandle:
    def __init__(self) -> None:
        self.__host = options_connection["HOST"]
        self.__port = options_connection["PORT"]
        self.__db = options_connection["DB"]
        self.__connection = None


    def connect(self) -> Redis:
            self.__connection = Redis(
                host= self.__host,
                port=self.__port,
                db=self.__db
            )
            return self.__connection
    
    def get_conn(self) -> Redis: 
        print(self.__connection) 
        return self.__connection
