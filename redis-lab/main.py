from redis import ConnectionPool, Redis




pool = ConnectionPool(host='127.0.0.1', port=6379, db=0)
redis_conn = Redis(connection_pool=pool)


pipe = redis_conn.pipeline()

pipe.set('a', 10)
pipe.set('b', 10)
pipe.execute()

pipe.set('a', 11)
pipe.set('b', 11)
pipe.execute()

