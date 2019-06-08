import getdata as gd
from FansList import FansList

def main(name="marctreu"):
    gd.generateData(name)

def load(name="caravels_lacuna"):
    return FansList.load(name)

if __name__ == "__main__":
    main("marctreu")
    #print(">")
    #main("ryukisai")
    #print ("Il y a "+str(len(disco[0][0]))+" album sur "+str(disco[0][1])+" dans la collection")
    #print ("Il y a "+str(len(disco[1][0]))+" album sur "+str(disco[1][1])+" dans la collection")
