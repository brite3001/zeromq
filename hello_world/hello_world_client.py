import zmq

print(f"Current libzmq version is {zmq.zmq_version()}")
print(f"Current  pyzmq version is {zmq.__version__}")

context = zmq.Context()

# talk to a server
print("Connecting to the Pirate Bay")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

for request in range(10):
    print(f"Sending request {request}...")
    socket.send_string("hello")

    # wait for reply
    message = socket.recv()
    print(f"Received message from Pirate Bay {message}")
