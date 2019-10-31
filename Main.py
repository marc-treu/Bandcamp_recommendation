from BandCampAPI import Fan, FanScroller
from Utils.utils import *
from Interface_terminal.interface import *


def create_fan():

    fan = FanScroller.get_data_initialise(formate_url(welcome()))
    res = FanScroller.get_discography(fan)
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



