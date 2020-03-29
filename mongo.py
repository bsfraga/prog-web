from pymongo import MongoClient
from utils.properties import Properties
import platform


class DbClient:

    def __init__(self):
        if platform.system() == 'Linux':
            path = ''
        elif platform.system() == 'Windows':
            path = 'C:\\Dev-Info\\info.properties'
            Properties.get_connection_properties()




        self.client = MongoClient()
