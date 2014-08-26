#!/usr/bin/python3


#standard modules
import configparser
import sys

#custom modules
#import communication


class Configuration:
    
    def __init__(self, section):
        self.configfile = 'config.ini'
        self.config = configparser.ConfigParser()  
         
        self.check_configfile() 
        self.initiate_configfile()
        
        self.configuration = self.read_section(section)    
        

    def check_configfile(self):
        try:
            self.config.read(self.configfile)

        except configparser.DuplicateOptionError:
            #communication.Communicate('Error in config file: {}'.format(sys.exc_info()[1]))
            exit()
            
            
    def read_section(self, section):
            return [option for option in self.config[section].values()]
            
            
    def initiate_configfile(self):
        if self.config.read(self.configfile) == []:
            self.config['path'] = {'path1': 'dummy'}
            self.config['time'] = {'format': '0'}
            with open(self.configfile, 'w') as configfile:
                self.config.write(configfile)
                
if __name__ == '__main__':
    x = Configuration('time')
    print(x.configuration)
