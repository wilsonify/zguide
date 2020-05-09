"""
Request-reply client in Python
Connects REQ socket to tcp://localhost:5559
Sends "Hello" to server, expects "World" back
"""

import zmq


def main():
    """
    Do 10 requests, waiting each time for a response
    :return:
    """
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5559")

    for request in range(1, 11):
        socket.send(b"Hello")
        message = socket.recv()
        print("Received reply %s [%s]" % (request, message))


if __name__ == "__main__":
    main()
