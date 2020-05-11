"""
Task ventilator
push tasks to workers
"""

import logging

import zmq
import random
import time


def main():
    context = zmq.Context()

    logging.info("send messages on 5557")
    sender = context.socket(zmq.PUSH)
    sender.bind("tcp://*:5557")

    logging.info("Sending tasks to workers")
    for task_nbr in range(10):
        workload = random.randint(1, 5)
        message_dict = {
            "task_nbr": task_nbr,
            "strategy": "strategy_one",
            "workload": workload
        }

        sender.send_json(message_dict)
        print(f"message_dict={message_dict}")
    for task_nbr in range(10):
        workload = random.randint(1, 5)
        message_dict = {
            "task_nbr": task_nbr,
            "strategy": "strategy_two",
            "workload": workload
        }

        sender.send_json(message_dict)
        print(f"message_dict={message_dict}")

    for task_nbr in range(10):
        workload = random.randint(1, 5)
        message_dict = {
            "task_nbr": task_nbr,
            "strategy": "strategy_three",
            "workload": workload
        }

        sender.send_json(message_dict)
        print(f"message_dict={message_dict}")


if __name__ == "__main__":
    main()
