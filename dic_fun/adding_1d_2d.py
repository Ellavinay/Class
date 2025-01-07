def value(a,b):
    b.update(a)
    return b
res=value({'a': 100, 'b': 200},{'x': 300, 'y': 200})
print(res)


def value(a,b,c):
    e={}
    for i in (a,b,c):
        e.update(i)
    return e
print(value({1: 10, 2: 20},{3: 30, 4: 40},{5: 50, 6: 60}))

