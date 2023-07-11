import os


def path(file_name):
    return os.path.abspath((os.path.dirname(__file__) + f'/image/{file_name}.jpeg'))
