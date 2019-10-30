from bs4 import BeautifulSoup
import json
import requests

from BandCampAPI.Fan import Fan


class FanScroller:

    @staticmethod
    def get_data_initialise(url):
        r = requests.get(url)
        if r.status_code != 200:
            return False
        soup = BeautifulSoup(r.content, features="html.parser")

        data = json.loads(soup.find('div', {'id': 'pagedata'})['data-blob'])

        fan = Fan(data['fan_data']['fan_id'], data['fan_data']['username'], data['fan_data']['trackpipe_url'],
                  data['fan_data']['location'], data['fan_data']['bio'], data['fan_data']['fav_genre'],
                  data['collection_data']['item_count'], data['wishlist_data']['item_count'])

        return fan