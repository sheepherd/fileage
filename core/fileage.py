import time
import os
import stat

import balloontip


class FileAge:
    # Class to check the fileage
    # Returns tooltip
    
    def __init__(self, path):
        # Initializes the tooltip
        # Caches the path
        # Runs the functions sequencially
        
        self.information = balloontip.WindowsBalloonTip
        self.path = path
        
        exists = self.check_existence()
        message = self.generate_message(exists)
        self.show_tooltip(message)

    def check_existence(self):
        # Checks if the file on given path exists
        # Returns True on success
        # Returns False on error
        
        try:
            open(self.path, 'r')
        except FileNotFoundError:
            return False
        else:
            return True

    def generate_message(self, exists):
        # Returns a message dependent on check_existence
        # The message contains the actual message and a title
        
        if exists == True:
            tmp = time.time() - os.stat(self.path)[stat.ST_MTIME]
            return [str(round(tmp/60,2)), 'File Age']
        elif exists == False:
            return ['Log file not found\nCheck the config.ini', 'Error']

    def show_tooltip(self, message):
        # Feeds the tooltip a message and title
        
        self.information(message[0], message[1])

# Path is still hardcoded, planned feature
FileAge(r'\\infsaa1012\ecprog_kba$\Outlook_Synch_Log\Logbuch.txt')
