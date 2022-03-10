from audioop import avg
import zmq
import time
from random import randrange

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5556")

postcode_filter = str(randrange(3000, 3005))
readings = 0
socket.setsockopt_string(zmq.SUBSCRIBE, postcode_filter)

temp_readings = []
while readings < 1000000:
    message = socket.recv_string()
    postcode, temperature, humidity = message.split()

    if postcode == postcode_filter:
        temp_readings.append(int(temperature))

    readings += 1

    # print(f"Messages received {readings}")

print(f"The average temperature for {postcode_filter}: {sum(temp_readings) / readings}")
print(f"Messages received {readings}")
