from BandCampAPI import Fan, FanScroller
from Utils.utils import *
from Interface_terminal.interface import *
import requests
from bs4 import BeautifulSoup
import json


def main():

    if check_data_exist():
        load_data()
    else:
        f = FanScroller.FanScroller.get_data_initialise(formate_url(welcome()))
        print(f)


if __name__ == '__main__':
    main()

    #marc = Fan.Fan(1234, 'Marc', 'aezRAR')



