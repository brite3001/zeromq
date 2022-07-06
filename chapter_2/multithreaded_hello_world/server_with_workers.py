import time
import threading
import zmq

def worker_routine(worker_url: str, worker_number: int, context: zmq.Context = None):
    print('meep')

    context = context or zmq.Context.instance()

    # socket to talk to the dispatcher
    socket = context.socket(zmq.REP)
    socket.connect(worker_url)

    while True:
        string = socket.recv()
        print(f"Received request: [ {string} ], Processed by Worker: {worker_number}")

        # 'work'
        time.sleep(1)

        socket.send(b'hello')

def main():
    """ server routine """

    url_worker = "inproc://workers"
    url_client = "tcp://*:5555"

    context = zmq.Context.instance()

    # socket to talk to clients
    client = context.socket(zmq.ROUTER)
    client.bind(url_client)

    workers = context.socket(zmq.DEALER)
    workers.bind(url_worker)
    print('zzzz')

    for i in range(5):
        thread = threading.Thread(target=worker_routine, args=(url_worker, i))
        thread.deamon = True
        thread.start()
    
    print('qqqq')

    zmq.proxy(client, workers)

    print('gg')

    clients.close()
    workers.close()
    context.term()

if __name__ == "__main__":
    main()