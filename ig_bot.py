from selenium import webdriver
import time
from random import seed
from random import randint
from selenium.webdriver.common.keys import Keys
import os
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
driver = webdriver.Edge()
# options = webdriver.ChromeOptions()
# options.headless = True
# options.add_argument(f'user-agent={user_agent}')
# options.add_argument("--window-size=1920,1080")
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--allow-running-insecure-content')
# options.add_argument("--disable-extensions")
# options.add_argument("--proxy-server='direct://'")
# options.add_argument("--proxy-bypass-list=*")
# options.add_argument("--start-maximized")
# options.add_argument('--disable-gpu')
# options.add_argument('--disable-dev-shm-usage')
# options.add_argument('--no-sandbox')
# driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
class InstaBot:
    def __init__(self, username, password):
        driver.implicitly_wait(30)
        driver.get("https://instagram.com")      
        time.sleep(getRandomTime())
        driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys('_gautambisht_11')
        driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys('e8c2cadf2148')
        time.sleep(getRandomTime())      
        driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()


        try:
             driver.implicitly_wait(30)
             notifications = driver.find_element_by_xpath('//button[text()="Not Now"]')
             notifications.click()
             time.sleep(1)
        except:
             driver.refresh()
             driver.implicitly_wait(30)
             time.sleep(6)
             notifications = driver.find_element_by_xpath('//button[text()="Not Now"]')
             notifications.click()
            

        try:
             driver.implicitly_wait(30)
             time.sleep(getRandomTime())
             driver.find_element_by_xpath('//button[text()="Not Now"]')\
                  .click()

        except:
             driver.refresh()
             driver.implicitly_wait(30)
             time.sleep(6)
             driver.find_element_by_xpath('//button[text()="Not Now"]')\
                  .click()
        
        try:
            driver.implicitly_wait(30)
            time.sleep(getRandomTime())
            search_2 = driver.find_element_by_xpath('//input[@placeholder="Search"]')
            search_2.send_keys('virat.kohli')
            time.sleep(6)
            search_2.send_keys(Keys.ENTER)   
            count = 0
            while count <2:
                search_2.send_keys(Keys.ENTER)
                count +=1 # count = count +1
                time.sleep(1)
        except:
            driver.refresh()
            time.sleep(getRandomTime())
            search_2 = driver.find_element_by_xpath('//input[@placeholder="Search"]')
            search_2.send_keys('virat.kohli')
            time.sleep(6)
            search_2.send_keys(Keys.ENTER)   
            count = 0
            while count <2:
                search_2.send_keys(Keys.ENTER)
                count +=1 # count = count +1
                time.sleep(1)
        time.sleep(getRandomTime())
        driver.implicitly_wait(30)
        follow = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/div/div/div/span/span[1]/button')
def getRandomTime():
        randTime = randint(3, 5)
        return randTime      
InstaBot("your_usernmae", "your_password")   

while (True):  
    try:
        follow = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/div/div/div/span/span[1]/button').click()
        print('Following')
        time.sleep(3)
        driver.implicitly_wait(30)
    except:
        pass
    try:
        unfollow1 = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/div/div[2]/div/span/span[1]/button').click()
        time.sleep(1)
        unfollow2 = driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[1]').click()
        print('Unfollowed')
        time.sleep(2)
        driver.refresh()
        print("Refreshing.")
        time.sleep(5)
        driver.save_screenshot("C:\\Users\\IS\\Videos\\Captures\\screenshot.png")
        print("Screenshot saved.")
    except:
        pass
        
