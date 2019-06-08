import pickle

class Discography:

    def __init__(self,name, albums=None):
        self.name = name
        self.albums = albums
        self.taille = 0 if albums == None else len(self.albums)

    def getNameFromAdresse(adresse):
        return adresse.split("/")[-1].split("?")[0]

    def __len__(self):
        return self.taille

    def getName(self):
        return self.name

    def getAlbumsCollection(self):
        return self.albums

    def load(name):
        return pickle.load(open('disco/'+name, 'rb'))

    def save(self):
        pickle.dump(self, open('disco/'+self.name, 'wb'))
