#!/usr/bin/python

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

        for x in path:
            exists = self.check_existence(x)
            message = self.generate_message(exists)
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

    def generate_message(self, exists):
        # Returns a message dependent on check_existence
        # The message contains the actual message and a title
        
        if exists[1] == True:
            tmp = time.time() - os.stat(exists[0])[stat.ST_MTIME]
            return 'File Age: ' + str(round(tmp/60,2))
        elif exists[1] == False:
            return 'Error: Log file not found. Check the config.ini'

    def show_tooltip(self, message):
        # Feeds the tooltip a message and title
        
        communication.Communicate(message)

configuration = config.Configuration()
FileAge(configuration.path)
