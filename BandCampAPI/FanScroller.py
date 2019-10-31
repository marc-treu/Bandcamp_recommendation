from bs4 import BeautifulSoup
import json
import requests

from BandCampAPI.Fan import Fan
from BandCampAPI.Album import Album


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

    @staticmethod
    def get_discography(fan):

        s = requests.session()

        header = {'Host': 'bandcamp.com', 'Referer': fan.get_url()}

        payload_col = {"fan_id": fan.get_id(), "older_than_token": "9999999999::a::",
                       "count": fan.get_length_collection()}

        collection_items = s.post('https://bandcamp.com/api/fancollection/1/collection_items',
                                  data=json.dumps(payload_col), headers=header).json()

        result = []

        for item in collection_items['items']:
            result.append(Album(item['band_id'], item['band_name'], item['album_id'], item['album_title'],
                                item['item_url'], item['genre_id'], item['also_collected_count']))

        payload_wish = {"fan_id": fan.get_id(), "older_than_token": "9999999999::a::",
                        "count": fan.get_length_wishlist()}

        wishlist_items = s.post('https://bandcamp.com/api/fancollection/1/wishlist_items',
                                data=json.dumps(payload_wish), headers=header).json()

        for item in wishlist_items['items']:
            result.append(Album(item['band_id'], item['band_name'], item['album_id'], item['album_title'],
                                item['item_url'], item['genre_id'], item['also_collected_count']))

        return result
