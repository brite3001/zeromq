import sys
import time
import zmq

context = zmq.Context()

# messeges are received here
receiver = context.socket(zmq.PULL)
receiver.connect("tcp://localhost:5557")

# messages are sent with this
sender = context.socket(zmq.PUSH)
sender.connect("tcp://localhost:5558")

while True:
    s = receiver.recv()

    sys.stdout.write(".")
    sys.stdout.flush()

    # the 'work'
    time.sleep(int(s) * 0.001)

    # send 'results' to the sink
    sender.send(b"")
