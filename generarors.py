def count():
    for i in range(4):
        yield i
g = count()
print(next(g))
print(next(g))
print(next(g))
