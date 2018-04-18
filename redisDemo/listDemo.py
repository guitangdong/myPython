import redis

#管理对redis的所有连接，避免每次建立、释放连接的开销。
pool = redis.ConnectionPool(host='localhost', port=6379)
#Redis实例
r = redis.Redis(connection_pool=pool)

if __name__ == '__main__':
    print('List 操作：')
    print('添加到List的最左边：')
    r.lpush('mylist',1)
    r.lpush('mylist',2)
    r.lpush('mylist',3)
    r.lpush('mylist',4)
    print(r.lrange('mylist',0,100))
    r.delete('mylist')

    print('添加到List的最右边：')
    r.rpush('mylist',1)
    r.rpush('mylist',2)
    r.rpush('mylist',3)
    r.rpush('mylist',4)
    print(r.lrange('mylist',0,100))

    print('输出最左边：')
    print(r.lpop('mylist'))
    print('输出最右边：')
    print(r.rpop('mylist'))
    print('输出剩余的：')
    print(r.lrange('mylist',0,100))
    r.delete('mylist')

