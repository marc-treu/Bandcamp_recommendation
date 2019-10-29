import os


def check_data_exist():
    """
    Just a checker, if a project had already began, it will have a data/ folder

    :return: True if the folder data is in the system, False otherwise
    """
    return "data" in os.listdir()


def initialise_system():
    if not check_data_exist():
        os.mkdir('data')
