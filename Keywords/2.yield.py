def generator(n):
    for i in range(0, n):
        yield i * 10


g = generator(5)
for i in g:
    print(i)
