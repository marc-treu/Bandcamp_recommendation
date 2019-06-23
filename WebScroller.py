import abc
import requests


class WebScroller(abc.ABCMeta):

    @abc.abstractmethod
    def get_data(self):
        pass


class FanWebScroller(WebScroller):

    @staticmethod
    def get_data(fan_list):
        return True

    @staticmethod
    def get_fan_data(fan):
        return True


class ArtistWebScroller(WebScroller):

    @staticmethod
    def get_data(artist_list):
        return True

    @staticmethod
    def get_fan_data(artist):
        return True

