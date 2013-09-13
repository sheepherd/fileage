import configparser


class Configuration:
    def __init__(self):
        config = configparser.ConfigParser


    def check_configfile(configfile):
        if config.read( == []:
            config['basic']['Path'] = '\\infsaa1012\ecprog_kba$\Outlook_Synch_Log\Logbuch.txt'
            config.write(configfile)
        else:
            return True


config = configparser.ConfigParser
configfile = 'config.ini'
Configuration.check_configfile(configfile)
