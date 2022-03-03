#!/usr/bin/python3

import os
import threading
import platform
import time
import logging

if platform.system().lower() == 'windows': ping_arg = '-n'
else: ping_arg = '-c'
logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] %(asctime)s - %(threadName)s: %(message)s')

i=0

logging.info('Starting...')
time.sleep(2)

def ping(host):
    try:
        global i
        if platform.system().lower() == 'windows':
            command = "ping {} 1 -w 2 {} >> null".format(ping_arg, host)
        else:
            command = "ping {} 1 -w 2 {} > /dev/null".format(ping_arg, host)

        while True:
            i+=1
            result = os.system(command) 
            #print(result)
            if result == 0:
                logging.info('Pings: {} -- {} is up.'.format(i, host))
            elif result == 2:
                logging.error('Detected Manual Interrupt. Ending.')
                exit()
            else:
                logging.warning('Pings: {} -- {} is down.'.format(i, host))
    except KeyboardInterrupt:
        exit()

for j in range(2400):
    try:
        time.sleep(0)
        ping_thread = threading.Thread(target=ping, args=('192.168.0.179',))
        ping_thread.start()
    except KeyboardInterrupt:
        exit()

def menu():
    print()
