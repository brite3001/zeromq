import zmq
from random import randrange
import time

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5556")


while True:
    zipcode = randrange(3000, 3005)
    temperature = randrange(2, 45)
    humidity = randrange(5, 100)

    socket.send_string(f"{zipcode} {temperature} {humidity}")
    time.sleep(0.1)
