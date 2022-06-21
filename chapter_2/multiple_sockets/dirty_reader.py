import zmq
import time

context = zmq.Context()

# connect to ventilator from ch1
receiver = context.socket(zmq.PULL)
receiver.connect("tcp://localhost:5557")

# connect to weather server from ch1
subscriber = context.socket(zmq.SUB)
subscriber.connect("tcp://localhost:5556")
subscriber.setsockopt(zmq.SUBSCRIBE, b"3003")

while True:

    while True:
        try:
            msg = receiver.recv(zmq.DONTWAIT)
            if msg:
                print(msg)
        except zmq.Again:
            break

    while True:
        try:
            msg = subscriber.recv(zmq.DONTWAIT)
            if msg:
                print(msg)
        except zmq.Again:
            break

    time.sleep(0.001)
