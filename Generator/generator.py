#生成器函数
def createGenerator():
    for i in range(1,4):
        yield i

if __name__ == '__main__':
    print('普通的数组')
    list = [1,2,3]

    print('第一次调用的情况下，输出：')
    for i in list:
        print(i)
    print('---------------------')
    print('第二次调用的情况下，重新输出值：')
    for i in list:
        print(i)
    print('---------------------')

    print('生成器表达式 使用的是()小括号')
    generator1 = (i for i in range(1,4))

    print('第一次调用的情况下，输出：')
    for i in generator1:
        print(i)
    print('---------------------')
    print('第二次调用的情况下，不在输出值：')
    for i in generator1:
        print(i)
    print('---------------------')

    print('生成器函数')
    generator2 = createGenerator()
    print('第一次调用的情况下，输出：')
    for i in generator2:
        print(i)
    print('---------------------')
    print('第二次调用的情况下，不在输出值：')
    for i in generator2:
        print(i)
    print('---------------------')