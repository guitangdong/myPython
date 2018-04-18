import redis

#管理对redis的所有连接，避免每次建立、释放连接的开销。
pool = redis.ConnectionPool(host='localhost', port=6379)
#Redis实例
r = redis.Redis(connection_pool=pool)

if __name__ == '__main__':
    print('String 操作：')
    print('设置单个键值对：')
    r.set('name', 'guitangdong')
    print(r.get('name'))
    r.delete('name')
    print(r.get('name'))

    print('设置多个键值对：')
    r.mset(name='guitangdong',sex='male')
    print(r.mget('name','sex'))
    r.delete('name')
    print(r.mget('name','sex'))
    r.delete('sex')
    print(r.mget('name','sex'))