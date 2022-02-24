import time
import zmq

print(f"Current libzmq version is {zmq.zmq_version()}")
print(f"Current  pyzmq version is {zmq.__version__}")

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    # wait for reply from client
    message = socket.recv()
    print(f"Received request: {message}")

    time.sleep(1)

    socket.send_string("World")
