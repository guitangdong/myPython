def createIdGenerator(startId):
    i = startId
    while True:
        yield i
        i = i + 1

if __name__ == '__main__':
    generator = createIdGenerator(100)
    for i in range(5):
        print(generator.__next__())

    print('---------------------')
    for i in range(5):
        print(generator.__next__())

    print('---------------------')