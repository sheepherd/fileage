#!/usr/bin/python3

import datetime

class Communicate:
    def __init__(self, message):
        self.output(message)
        self.logfile(message)
    
    def output(self, message):
        print(message)
    
    def logfile(self, message):
        timestamp = datetime.datetime.today()
        with open('logfile.txt', 'a') as logfile:
            logfile.write(str(timestamp) + ' ' + message + '\n')
        
if __name__ == '__main__':
    message = 'test'
    Communication(message)
