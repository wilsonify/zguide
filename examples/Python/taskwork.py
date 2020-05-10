"""
Task worker
Collect workload from ventilator
Sends results to sink
"""

import logging
import time

import zmq


def main():
    context = zmq.Context()
    logging.info("receive messages on 5557")
    vent = context.socket(zmq.PULL)
    vent.connect("tcp://localhost:5557")

    logging.info("send messages to 5558")
    sink = context.socket(zmq.PUSH)
    sink.connect("tcp://localhost:5558")

    while True:
        print("waiting for message")
        message_dict = vent.recv_json()
        print(f"start message_dict={message_dict}")
        time.sleep(message_dict['workload'])
        print(f"done message_dict={message_dict}")
        sink.send_json(message_dict)


if __name__ == "__main__":
    main()
