from Discography import Discography
from FansList import FansList
import re
import selenium.webdriver
import time
import urllib.request

class Webscroller:

    def __init__(self):

        self.profile = selenium.webdriver.FirefoxProfile()                      # creation of the profile
        self.profile.set_preference("permissions.default.image", 2)

        self.driver = None
        self.isopen = False

    def openDriver(self):
        self.driver = selenium.webdriver.Firefox(firefox_profile=self.profile)  # creation of the driver
        self.isopen = True

    def removeDoublon(self,collection):
        result = set()
        for i in range(len(collection)):
            if collection[i][0]!="h": result.add("https://"+collection[i])
            else: result.add(collection[i])
        return result

    def getDiscography(self,name):
        """
        return an object Discography
        """
        nbCollection,nbWishList = Webscroller.getNumberDisco(name)

        collection = self.getCollectionFromDriver("https://bandcamp.com/"+name,nbCollection) \
                 if nbCollection > 45 else \
                 self.getCollectionFromUrllib("https://bandcamp.com/"+name)


        wishList = self.getCollectionFromDriver("https://bandcamp.com/"+name+"/wishlist",nbWishList)\
                if nbWishList > 45 else \
                self.getCollectionFromUrllib("https://bandcamp.com/"+name+"/wishlist")

        collection = self.removeDoublon(collection)
        wishList = self.removeDoublon(wishList)

        return Discography(name,collection.union(wishList))

    def getNumberDisco(name):
        """
        open with urllib a fan page, and return the number of albums in
        his collection and in his wishlist
        """
        with urllib.request.urlopen("https://bandcamp.com/"+name) as discoHtml:
            html = discoHtml.read()
        result = re.findall(r'<span class="count">(\d*)</span>',str(html))
        return int(result[0]),int(result[1])

    def getCollectionFromDriver(self,adresse,nbElement):
        """
        Renvoie la collection presente sur la page d'un utilisateur avec Driver
        """
        if not self.isopen: # Si le driver n'est pas encore ouvert
            self.openDriver()
        try:
            self.driver.get(adresse)
            self.driver.find_element_by_xpath("(//button[@class='show-more'])[1]").click()
        except selenium.common.exceptions.ElementNotInteractableException:
            try:
                self.driver.find_element_by_xpath("(//button[@class='show-more'])[2]").click()
            except:
                pass
        for j in range(int((nbElement/40)*1.35)+1):
            self.driver.execute_script("window.scrollBy(0, 5000);")
            time.sleep(1)

        return [element.get_attribute('href') for element in self.driver.find_elements_by_xpath("(//a[@class='item-link'])")]

    def getCollectionFromUrllib(self,adresse):
        """
        Renvoie la collection presente sur la page d'un utilisateur avec urllib
        """
        with urllib.request.urlopen(adresse) as discoHtml:
            html = discoHtml.read()
        return re.findall(r'<a target="\S*?" href="(\S*?)" class="item-link">',str(html))

    def getFanslist(self,adresse):

        fans = self.getFansBaseFromDriver(adresse) \
                if self.isMoreFans(adresse) else \
                self.getFansBaseFromUrllib(adresse)

        return FansList(adresse,fans)


    def isMoreFans(self,adresse):
        """
        open with urllib a album page, and return True if you need to push the more
        button or False if not
        """
        with urllib.request.urlopen(adresse) as albumHtml:
            html = albumHtml.read()
        result = re.findall(r'more-thumbs|more-writing',str(html))
        return True if result != [] else False

    def getFansBaseFromDriver(self,adresse):
        """
        Renvoie la liste des utilisateurs qui ont acheter l'album,
        genere avec un Driver
        """
        if not self.isopen: # Si le driver n'est pas encore ouvert
            self.openDriver()
        try:
            self.driver.get(adresse)
            while 1:
                # tant que l'on peut etendre la liste des utilisateurs, on clique
                self.driver.find_element_by_xpath("(//a[@class='more-writing'])[1]").click()
                time.sleep(2)
        except: pass
        try:
            while 1:
                self.driver.find_element_by_xpath("(//a[@class='more-thumbs'])[1]").click()
                time.sleep(2)
        except: pass
        time.sleep(2)
        # Lorsque l'on a fini de cliquer sur tous les mores, on peut renvoyer la liste des utilisateurs
        tmp1 = [element.get_attribute('href') for element in self.driver.find_elements_by_xpath("(//a[@class='pic'])")]
        tmp2 = [element.get_attribute('href') for element in self.driver.find_elements_by_xpath("(//a[@class='fan pic'])")]
        return tmp1 + tmp2

    def getFansBaseFromUrllib(self,adresse):
        """
        Renvoie la liste des utilisateurs qui ont acheter l'album,
        genere avec un urllib
        """
        with urllib.request.urlopen(adresse) as albumHtml:
            html = albumHtml.read()
        fansComment = re.findall(r'class="name notSkinnable" href="(\S*?)"',str(html))
        fans = re.findall(r'<a class="fan pic" href="(\S*?)"',str(html))
        print(fans[:5])
        return fansComment+fans


    def close(self):
        """
        Close the driver
        """
        if self.isopen:
            self.driver.close()
