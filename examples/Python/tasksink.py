"""
Task sink
Collects results from workers
"""

import logging

import zmq


def main():
    context = zmq.Context()

    logging.info("receive messages on 5558")
    receiver = context.socket(zmq.PULL)
    receiver.bind("tcp://*:5558")

    logging.info("Wait for start of batch")
    s = receiver.recv()

    while True:
        print("waiting for next message")
        message_dict = receiver.recv_json()
        print(f"message_dict={message_dict}")


if __name__ == "__main__":
    main()
