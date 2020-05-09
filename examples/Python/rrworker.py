#
#   Request-reply service in Python
#   Connects REP socket to tcp://localhost:5560
#   Expects "Hello" from client, replies with "World"
#
import zmq


def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.connect("tcp://localhost:5560")

    while True:
        message = socket.recv()
        print("Received request: %s" % message)
        socket.send(b"World")


if __name__ == "__main__":
    main()
