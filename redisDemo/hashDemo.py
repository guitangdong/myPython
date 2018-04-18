import redis

#管理对redis的所有连接，避免每次建立、释放连接的开销。
pool = redis.ConnectionPool(host='localhost', port=6379)
#Redis实例
r = redis.Redis(connection_pool=pool)

if __name__ == '__main__':
    print('Hash 操作：')
    print('在hash中设置一个键值对：')
    r.hset('author','name','guitangdong')
    r.hset('author','sex','male')
    print(r.hgetall('author'))
    print(r.hget('author','name'))
    r.hdel('author','sex')
    print(r.hgetall('author'))
    r.hdel('author','name')
    print(r.hgetall('author'))
    r.delete('author')
    print(r.hgetall('author'))

    print('在hash中批量设置键值对：')
    r.hmset('author',{'name':'guitangdong','sex':'male'})
    print(r.hgetall('author'))
    print(r.hget('author','name'))
    r.delete('author')
    print(r.hgetall('author'))
