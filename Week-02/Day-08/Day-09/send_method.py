def echo():
    received = yield "Start"
    while True:
        received = yield f"Received: {received}"

g = echo()
print(next(g))  # Starts generator, yields "Start"
print(g.send("Ping!")) # Yields "Received: Ping!"
print(g.send("Pong!")) # Yields "Received: Pong!"