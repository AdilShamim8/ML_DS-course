def running_average():
    count, total = 0, 0.0
    avg = None
    while True:
        new = yield avg
        count += 1
        total += new
        avg = total / count

g = running_average()
print(next(g))        # Start generator; yields None
print(g.send(10))     # 10.0
print(g.send(20))     # 15.0
print(g.send(30))     # 20.0