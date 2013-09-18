#!/usr/bin/python


import configparser


class Configuration:
    def __init__(self):
        configfile = 'config.ini'
        self.path = self.check_configfile(configfile)

    def check_configfile(self, configfile):
        config = configparser.ConfigParser()
        if config.read(configfile) == []:
            config['basic'] = {'path': 'dummyfile.ini'}
            with open('config.ini', 'w') as configfile:
                config.write(configfile)
                return config['basic']['path']
        else:
            return config['basic']['path']
