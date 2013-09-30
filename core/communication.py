#!/usr/bin/python3

import datetime

class Communicate:
    def __init__(self, message):
        string = ''
        last_line = len(message)
        current_line = 1
        
        for x in message:
            if current_line == last_line:
                string+=str(x)
            else:
                string+=str(x) + '\n'
                
            current_line+=1
            
        self.output(string)
        self.logfile(message)
    
    def output(self, string):
        print(string)
    
    def logfile(self, message):
        timestamp = datetime.datetime.today()
        
        with open('logfile.txt', 'a') as logfile:
            for x in message:
                logfile.write(str(timestamp) + ' ' + x + '\n')
        
if __name__ == '__main__':
    message = ['test1', 'test2']
    Communicate(message)
