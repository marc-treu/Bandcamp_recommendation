import re
import selenium.webdriver
import time
import numpy

def main():
    
    profile = selenium.webdriver.FirefoxProfile()
    profile.set_preference("permissions.default.image", 2)
    driver = selenium.webdriver.Firefox(firefox_profile=profile)

    driver.get("https://bandcamp.com/marctreu")
    try:
        driver.find_element_by_class_name('show-more').click()
        time.sleep(2)
        for i in range(1):
            driver.execute_script("window.scrollBy(0, 4000);")
            time.sleep(1)
    except:
        pass
    html_collection = str(driver.page_source)

    
    driver.get("https://bandcamp.com/marctreu/wishlist")
    time.sleep(3)
    driver.execute_script("window.scrollBy(0, 10000);")
    time.sleep(3)
    try:
        driver.find_element_by_xpath("(//button[@class='show-more'])[2]").click()
    except selenium.common.exceptions.ElementNotInteractableException:
        driver.find_element_by_xpath("(//button[@class='show-more'])[1]").click()

    time.sleep(2)
    for j in range(3):
        driver.execute_script("window.scrollBy(0, 4000);")
        time.sleep(1)
    html_wishlist = str(driver.page_source)
    
    driver.close()


    t = re.findall(r'music.[\w-]*.com/album/[\w-]*|https://[\w-]*.bandcamp.com/album/[\w-]*|https://music.[\w\-]*.com/album/[\w-]*',html_collection)
    t2 = re.findall(r'music.[\w-]*.com/album/[\w-]*|https://[\w-]*.bandcamp.com/album/[\w-]*|https://music.[\w\-]*.com/album/[\w-]*',html_wishlist)
    
    print("Il y a "+str(len(set(t)))+" album différent acheter et "+str(len(set(t2)))+" dans la wishlist")

    t = list(set().union(t,t2))
    for i in range(len(t)):
        print(t[i])


if __name__ == "__main__":
    #main()
    t = open("t.txt","r")
    lT = [i[0:-1] for i in t]
    t2 = open("t2.txt","r")
    lT2 = [i[0:-1] for i in t2]
    #print(lT[430])
    #print(lT2[428])
    setT = {lT[i] for i in range(431,len(lT)) }
    setT2 = {lT2[i] for i in range(429,len(lT2))}
    for i in setT-setT2:
        print(i)
    
