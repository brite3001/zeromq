import signal
import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5558")

try:
    socket.recv()
except KeyboardInterrupt:
    print("Interrupt received, stopping...")
finally:
    socket.close()
    context.term()