#!/usr/bin/env python
import threading, logging, time
import multiprocessing
from random import randint

from kafka import KafkaProducer


class Producer(threading.Thread):
    daemon = True

    def run(self):
        producer = KafkaProducer(bootstrap_servers='localhost:9092')
        count=0
        while True:
            ran=randint(0,9)
            count+=1
            final=[str(ran),str(count)]
            producer.send('cassie', str(', '.join(final)))

            time.sleep(1)


def main():
    tasks = [
        Producer()
    ]

    for t in tasks:

        t.start()


    time.sleep(150)

if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
        level=logging.INFO
        )
    main()