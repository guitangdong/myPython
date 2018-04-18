import redis

#管理对redis的所有连接，避免每次建立、释放连接的开销。
pool = redis.ConnectionPool(host='localhost', port=6379)
#Redis实例
r = redis.Redis(connection_pool=pool)

if __name__ == '__main__':
    print('Set 操作：')
    r.sadd('myset1',1,2,3,4)
    print(r.smembers('myset1'))
    r.sadd('myset2',3,4,5,6)
    print(r.smembers('myset2'))
    print('输出第一个set中存在，而其他set中不存在的：')
    print(r.sdiff('myset1','myset2'))
    print('输出2个集合的交集')
    print(r.sinter('myset1','myset2'))
    print('输出2个集合的并集')
    print(r.sunion('myset1','myset2'))
    r.delete('myset1')
    r.delete('myset2')
