from configparser import ConfigParser


class Properties:

    def __init__(self):
        self.parser = ''

    def get_connection_properties(self, path):
        with open(path, 'r') as file:
            while file.readline() is not None:
                pass
