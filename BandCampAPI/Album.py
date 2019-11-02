

class Album:

    def __init__(self, band_id, band_name, band_url, album_id, album_name, album_url, genre_id, collected_count):
        self.band_id = band_id
        self.band_name = band_name
        self.band_url = Album.https(band_url)
        self.album_id = album_id
        self.album_name = album_name
        self.album_url = Album.https(album_url)
        self.genre_id = genre_id
        self.collected_count = collected_count
        self.fans = False

    def is_fill(self):
        return self.fans is not False

    def get_band_id(self):
        return self.band_id

    def get_band_url(self):
        return self.band_url

    def get_band_url_short(self):
        return self.band_url[8:]

    def get_album_id(self):
        return self.album_id

    def get_album_url(self):
        return self.album_url

    def get_collected_count(self):
        return self.collected_count

    def __repr__(self):
        return str(self.__dict__)

    @staticmethod
    def https(url):
        return 'https' + url[4:] if not url.startswith('https') else url
