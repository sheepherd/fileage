#!/usr/bin/python

import configparser


class Configuration:
    def __init__(self):
        config = configparser.ConfigParser()


    def check_configfile(configfile):
        if config.read(configfile) == []:
            config['basic'] = {'Path': ''}
            with open('config.ini', 'w') as configfile:
                config.write(configfile)
            print('no config')
        else:
            print('config existent')
            return True


config = configparser.ConfigParser()
configfile = 'config.ini'
Configuration.check_configfile(configfile)
