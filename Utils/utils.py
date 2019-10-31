import os
import pickle as pkl


def check_data_exist():
    """
    Just a checker, if a project had already began, it will have a data/ folder

    :return: True if the folder data is in the system, False otherwise
    """
    return "data" in os.listdir()


def initialise_system():
    if not check_data_exist():
        os.mkdir('data')


def formate_url(url):
    if 'bandcamp.com' in url:
        return url
    return "https://bandcamp.com/" + url


def load_data():
    pass


def save_data(data, data_id):
    return pkl.dump(data,  open('data/' + data_id, 'wb'))


def create_data_base():
    os.mkdir('data')
