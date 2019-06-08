import pickle

class FansList:

    def __init__(self,adresse,fans):
        self.adresse = adresse
        self.fans = fans
        self.name = FansList.getNameFromAdresse(self.adresse)

    def getNameFromAdresse(adresse):
        names = adresse.split("/")
        return names[2].split(".")[0]+"_"+names[-1]

    def getAdresse(self):
        return self.adresse

    def getName(self):
        return self.name

    def getFans(self):
        return self.fans

    def load(name):
        return pickle.load(open('fansbase/'+name, 'rb'))

    def save(self):
        pickle.dump(self, open('fansbase/'+self.name, 'wb'))
