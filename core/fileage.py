#!/usr/bin/python3

import time
import os
import stat

# custom classes
import config
import communication


class FileAge:
    # Class to check the fileage
    # Returns tooltip
    
    def __init__(self, path):
        # Initializes the tooltip
        # Caches the path
        # Runs the functions sequencially

        message = []

        for x in path:
            exists = self.check_existence(x)
            message.append(self.generate_message(exists))
        
        self.show_tooltip(message)
    
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
            return 'File Age: ' + str(round(tmp/60,2))
        elif exists[1] == False:
            return 'Error: Log file not found. Check the config.ini'

    def show_tooltip(self, message):
        communication.Communicate(message)

if __name__ == '__main__':
    FileAge(config.Configuration('path').configuration)
