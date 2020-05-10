"""
Task worker
Collect workload from ventilator
Sends results to sink
"""

import logging
import time

import zmq

from types import MethodType


class Strategy:
    """The Strategy Pattern class"""

    def __init__(self, function):
        self.name = "Default Strategy"
        self.execute = MethodType(function, self)


def strategy_one(self, payload):
    """
    # Replacement method 1
    :param self:
    :return:
    """
    self.name = "Strategy One"
    time.sleep(payload['workload'])
    print("{} is used to execute method 1".format(self.name))


def strategy_two(self, payload):
    """
    # Replacement method 2
    :param self:
    :return:
    """
    self.name = "Strategy Two"
    time.sleep(payload['workload'])
    print("{} is used to execute method 2".format(self.name))


def strategy_three(self, payload):
    """
    # Replacement method 3
    :param self:
    :return:
    """
    self.name = "Strategy Three"
    time.sleep(payload['workload'])
    print("{} is used to execute method 2".format(self.name))


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
        strategy_str = message_dict['strategy'] if 'strategy' in message_dict else "strategy_one"
        curr_strategy = Strategy(eval(strategy_str))
        try:
            curr_strategy.execute(message_dict)
            message_dict['result'] = 'done'
            sink.send_json(message_dict)
            print(f"done message_dict={message_dict}")
        except:
            message_dict['result'] = 'failed'
            sink.send_json(message_dict)
            print("failed")


if __name__ == "__main__":
    main()
