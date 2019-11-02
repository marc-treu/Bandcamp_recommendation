from BandCampAPI import Fan, Scrapper
from Utils.utils import *
from Interface_terminal.interface import *


def create_fan():

    fan = Scrapper.get_data_fan(formate_url(welcome()))
    res = Scrapper.get_discography(fan)
    fan.fill(res)
    create_data_base()
    save_data(fan, fan.get_name())
    return fan


def main():

    # We load or create the fan collection
    fan = load_data() if check_data_exist() else create_fan()


if __name__ == '__main__':
    main()

    #marc = Fan.Fan(1234, 'Marc', 'aezRAR')



