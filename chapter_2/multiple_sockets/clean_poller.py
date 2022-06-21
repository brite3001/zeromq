import zmq

context = zmq.Context()

# connect to ventilator
receiver = context.socket(zmq.PULL)
receiver.connect("tcp://localhost:5777")

# connect to the weather server
subscriber = context.socket(zmq.SUB)
subscriber.connect("tcp://localhost:5556")
subscriber.setsockopt(zmq.SUBSCRIBE, b"3003")

poller = zmq.Poller()
poller.register(receiver, zmq.POLLIN)
poller.register(subscriber, zmq.POLLIN)

while True:
    try:
        socks = dict(poller.poll())
    except KeyboardInterrupt:
        break

    if receiver in socks:
        message = receiver.recv()
        print(f"Ventilator Message: {message}")
        # do the thing here if got message from receiver

    if subscriber in socks:
        message = subscriber.recv()
        print(f"Weather Message: {message}")
        # do the weather update thing here