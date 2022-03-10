import zmq
import random
import time

context = zmq.Context()

sender = context.socket(zmq.PUSH)
sender.bind("tcp://*:5557")

# used to sync start time with sink
sink = context.socket(zmq.PUSH)
sink.connect("tcp://localhost:5558")

print("Press enter when the workers are ready")
_ = input()
print("Sending tasks to workers")

sink.send(b"0")

random.seed()

total_ms_of_given_work = 0

for given_tasks in range(100):
    workload = random.randint(1, 100)
    total_ms_of_given_work += workload

    sender.send_string(f"{workload}")

print(f"Total expected cost: {total_ms_of_given_work} ms")

time.sleep(1)
