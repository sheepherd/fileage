#!/usr/bin/python3

# standard library
import time
import os
import stat
import logging

# custom classes
import config

class FileAge:
    # Class to check the fileage
    # Returns tooltip
    
    def __init__(self, path):
        # Caches the path
        # Runs the functions sequencially

        logging.basicConfig(filename='fileage.log', level=logging.DEBUG)

        for x in path:
            message = self.generate_message(self.check_existence(x))
            logging.info(message)
            print(message)
        
    def check_existence(self, path):
        # Checks if the file on given path exists
        # Returns True on success
        # Returns False on error
        
        try:
            open(path, 'r')
        except FileNotFoundError:
            return [path, False]
        else:
            return [path, True]
            
            
    def time_format(self):
        config_time = config.Configuration('time').configuration
        if config_time[0] == str(0):
            return time.time()

    def generate_message(self, exists):
        # Returns a message dependent on check_existence
        # The message contains the actual message and a title
        
        if exists[1] == True:    
            tmp = self.time_format() - os.stat(exists[0])[stat.ST_MTIME]
            return exists[0] + ' ' + str(round(tmp/60,2))
        elif exists[1] == False:
            return 'File not found. Check the config.ini'

if __name__ == '__main__':
    FileAge(config.Configuration('path').configuration)
