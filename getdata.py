from Discography import Discography
from FansList import FansList
import os
import time
from Webscroller import Webscroller


def generateDisco(name,wbs):
    if os.path.isfile('disco/'+name):
        print("The discography of "+name+" is already build")
        disco = Discography.load(name)
    else:
        print("Construction of the discography")
        disco = wbs.getDiscography(name)
        print(name+" discography is create")
        disco.save()
        print(name+" discography is save")
    return disco

def generateFansList(adresse,wbs):
    name = FansList.getNameFromAdresse(adresse)
    if os.path.isfile('fansbase/'+name):
        print("The liste of "+name+" is already build")
        fansList = FansList.load(name)
    else:
        print("Construction of fans list for\n"+adresse)
        fansList = wbs.getFanslist(adresse)
        print(name+" fans list is create")
        fansList.save()
        print(name+" fans list is save")
    return fansList

def generateData(name):
    wbs = Webscroller()
    disco = generateDisco(name,wbs)

    albums = list(disco.getAlbumsCollection())
    for i in range(len(albums)):
        print("\n///////////////  "+str(i+1)+" sur "+str(len(albums))+"   ///////////////\n")
        generateFansList(albums[i],wbs)

    fan = generateFansList(albums[0],wbs)
    print(fan.name)
    fans = fan.getFans()
    tick = time.time()
    for i in range(len(fans)):
        print("\n///////////////  "+str(i+1)+" sur "+str(len(fans))+"   ///////////////\n")
        nameFan = Discography.getNameFromAdresse(fans[i])
        generateDisco(nameFan,wbs)
        tack = time.time()
        print(str(tack-tick)+" ms depuis le debut")
        print("avec une moyenne de "+str((tack-tick)/(i+1)))

    tack = time.time()
    print(str(tack-tick)+" ms")
    wbs.close()
    #print(wbs.getAlbum("https://monolithmonolith.bandcamp.com/album/split-7"))
