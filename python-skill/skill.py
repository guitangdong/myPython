

if __name__ == '__main__':
    #批量赋值
    a,b,c = 1,3,5
    print(a,b,c)
    #交换赋值
    a,b,c = b,c,a
    print(a,b,c)
    #扩展拆箱
    a,*b,c = 1,3,5,7,9
    print(a,b,c)
    #区间操作
    print('是否在区间内：'+str(1<a<10))
    print('是否在区间内：'+str(1<c<10))

    #三元操作符来进行条件赋值
    d = 1 if False else 2
    print(d)

    #
    dict= {i: i *i for i in range(5) }
    set= {i *2 for i in range(5) }
    print(dict)
    print(set)

    a='guitangdong'
    #索引取值
    print(a[5])
    #切割字符串 负数表面从尾部开始计数
    print(a[0:2])
    print(a[0:-1])
    #指定步长切割字符串
    print(a[::2])
    #字符串倒置
    print(a[::-1])
    #循环输出
    print(a*4)

    #列表操作
    list = [0,1,2,3,4]
    #切割赋值
    list[1:1] = [0,0]
    print(list)
    #翻转列表
    list.reverse()
    print(list)


