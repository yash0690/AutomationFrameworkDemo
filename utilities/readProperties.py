import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig():
    # we can access getApplicationURL directly using class name without creating any object
    @staticmethod
    def getApplicationURL():
       url = config.get('common info','baseUrl')
       return url

    @staticmethod
    def getUseremail():
        username = config.get('common info','username')
        return username
    @staticmethod
    def getPassword():
        password = config.get('common info','password')
        return password
