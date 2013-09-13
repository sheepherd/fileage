import configparser

config = configparser.ConfigParser()
if config.read('config.ini') == []:
    print('empty')

class Configuration():
    def __init__(self):
        config = configparser.ConfigParser()
        configfile = 'config.ini'

        

    def check_configfile(self, configfile):
        if config.read(configfile) == []:
            config['basic']['Path'] = '\\infsaa1012\ecprog_kba$\Outlook_Synch_Log\Logbuch.txt'
            config.write(configfile)
