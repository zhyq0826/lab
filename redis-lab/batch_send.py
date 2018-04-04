from redis import ConnectionPool, Redis
import os


pool = ConnectionPool(host='127.0.0.1', port=6379, db=0)
redis_conn = Redis(connection_pool=pool)


def p():
    # 4s
    for i in range(10000000):
        redis_conn.lpush('push', i)


def c():
    # 5s 5000,000 200s
    while redis_conn.lpop('push'):
        pass


if __name__ == '__main__':
    pid = os.fork()
    if pid:
        c()
    else:
        c()
