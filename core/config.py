#!/usr/bin/python3


import configparser
import sys

import communication


class Configuration:
    def __init__(self):
        configfile = 'config.ini'   
        self.path = self.check_configfile(configfile)       

    def check_configfile(self, configfile):
        config = configparser.ConfigParser()
        options = {}
        try:
            config.read(configfile)

        except configparser.DuplicateOptionError:
            communication.Communicate('Error in config file: {}'.format(sys.exc_info()[1]))
            exit()
            
        if config.read(configfile) == []:
            config['path'] = {'path1': 'dummyfile.ini'}
            with open('config.ini', 'w') as configfile:
                config.write(configfile)
                return[option for option in config['path'].values()]
        else:
            return [option for option in config['path'].values()]

                
if __name__ == '__main__':
    x = Configuration()
    print(x.path)
