import sys
import time
import zmq

context = zmq.Context()

receiver = context.socket(zmq.PULL)
receiver.bind("tcp://*:5558")

# wait for a message from the sink before starting
s = receiver.recv()

tstart = time.time()

for task_number in range(100):
    s = receiver.recv()

    if task_number % 10 == 0:
        sys.stdout.write(":")
    else:
        sys.stdout.write(".")

        sys.stdout.flush()

tend = time.time()

print(f"Total work time: {(tend-tstart) * 1000} ms")
