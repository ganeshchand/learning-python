from clock import Clock
x = Clock()
print(x)
for i in xrange(10000):
    x.tick()
print(x)