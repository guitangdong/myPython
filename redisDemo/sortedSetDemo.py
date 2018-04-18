import redis

#管理对redis的所有连接，避免每次建立、释放连接的开销。
pool = redis.ConnectionPool(host='localhost', port=6379)
#Redis实例
r = redis.Redis(connection_pool=pool)

if __name__ == '__main__':
    print('Sorted Set 操作：')
    r.zadd('myset1','A',1,'B',2)
    r.zadd('myset2','B',2,'C',3)

    print('通过索引区间返回有序集合成指定区间内的成员:')
    print(r.zrange('myset1',0,100))
    print(r.zrange('myset2',0,100))

    print('通过字典区间返回有序集合的成员:')
    print('[为包含')
    print(r.zrangebylex('myset1','-','[B'))
    print(r.zrangebylex('myset2','-','[B'))
    print('(为不包含')
    print(r.zrangebylex('myset1','-','(B'))
    print(r.zrangebylex('myset2','-','(B'))

    print('通过分数返回有序集合指定区间内的成员:')
    print(r.zrangebyscore('myset1','0','2'))
    print(r.zrangebyscore('myset2','0','2'))
    print('(为不包含')
    print(r.zrangebyscore('myset1','0','(2'))
    print(r.zrangebyscore('myset2','0','(2'))

    r.delete('myset1')
    r.delete('myset2')
