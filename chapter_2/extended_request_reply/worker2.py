import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.connect("tcp://localhost:5560")

while True:
    message = socket.recv()
    print(f"Received request: {message}")
    socket.send(b"Hello from worker 2!")

