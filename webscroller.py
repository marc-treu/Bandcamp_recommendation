from Discography import Discography
from FansList import FansList
import re
import selenium.webdriver
import time
import urllib.request

def getHtmlCodeCollection(driver,nbElement):
    """
    Renvoie la collection presente sur la page d'un utilisateur
    """
    # TODO: si la page est petite pas besoin d'utilier le driver
    if nbElement < 45:
        return [element.get_attribute('href') for element in driver.find_elements_by_xpath("(//a[@class='item-link'])")]
    else:
        try:
            driver.find_element_by_xpath("(//button[@class='show-more'])[1]").click()
        except selenium.common.exceptions.ElementNotInteractableException:
            driver.find_element_by_xpath("(//button[@class='show-more'])[2]").click()

        for j in range(int((nbElement/40)*1.35)+1):
            driver.execute_script("window.scrollBy(0, 5000);")
            time.sleep(1)

        return [element.get_attribute('href') for element in driver.find_elements_by_xpath("(//a[@class='item-link'])")]

def parceHtmlCollection(htmlCode):
    """
    Parce le code HTML d'une page pour trouver tous les album acheter ou souhaiter
    """
    return re.findall(r'music.[\w-]*.com/album/[\w-]*|https://[\w-]*.bandcamp.com/album/[\w-]*|https://music.[\w\-]*.com/album/[\w-]*',htmlCode)

def getHtmlCodeAlbum(driver):
    """
    Renvoie la liste des utilisateurs qui ont acheter l'album
    """
    try:
        while 1:
            # tant que l'on peut etendre la liste des utilisateurs
            # on clique
            driver.find_element_by_xpath("(//a[@class='more-writing'])[1]").click()
            time.sleep(2)
    except:
        pass
    try:
        while 1:
            driver.find_element_by_xpath("(//button[@class='more-thumbs'])[1]").click()
            time.sleep(2)
    except:
        pass

    # Lorsque l'on a fini de cliquer sur tous les more, on peut renvoyer la liste des utilisateurs
    tmp1 = [element.get_attribute('href') for element in driver.find_elements_by_xpath("(//a[@class='pic'])")]
    print(tmp1)
    tmp2 = [element.get_attribute('href') for element in driver.find_elements_by_xpath("(//a[@class='fan pic'])")]
    return tmp1 + tmp2

def removeDoublon(collection):
    result = set()
    for i in range(len(collection)):
        if collection[i][0]!="h": result.add("https://"+collection[i])
        else: result.add(collection[i])
    return result

def getdiscography(name):

    profile = selenium.webdriver.FirefoxProfile()
    profile.set_preference("permissions.default.image", 2)
    driver = selenium.webdriver.Firefox(firefox_profile=profile)

    driver.get("https://bandcamp.com/"+name)
    nbCollection = int(driver.find_element_by_xpath("(//span[@class='count'])[1]").get_attribute('innerHTML'))
    nbWishList = int(driver.find_element_by_xpath("(//span[@class='count'])[2]").get_attribute('innerHTML'))

    htmlCollection = getHtmlCodeCollection(driver,nbCollection)

    driver.get("https://bandcamp.com/"+name+"/wishlist")

    htmlWishList = getHtmlCodeCollection(driver,nbWishList)
    driver.close()

    collection = removeDoublon(htmlCollection)
    wishList = removeDoublon(htmlWishList)
    collection.union(wishList)

    return Discography(name,collection.union(wishList))

def getAlbum(adresse):

    profile = selenium.webdriver.FirefoxProfile()
    profile.set_preference("permissions.default.image", 2)
    driver = selenium.webdriver.Firefox(firefox_profile=profile)

    driver.get(adresse)

    fans = FansList(adresse,getHtmlCodeAlbum(driver))
    driver.close()
    return fans

def getFullAlbumCollection(listAlbum):

    for album in listAlbum:
        # Pour chaque album de notre liste, on recu
        with urllib.request.urlopen(album) as albumHtml:
            html = response.read()
    return

if __name__ == "__main__":
    disco = getdiscography("ryukisai")
    print(len(disco[0][0]))
    print(disco[0][1])
    print(len(disco[1][0]))
    print(disco[1][1])
