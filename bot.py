from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import os
from random import seed
from random import randint

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
while True:
     print('Starting')
     driver.get('''https://www.youtube.com/watch?v=LVYMwW79j6Q''')
     time.sleep(15)
     browser.execute_script('''window.open("https://www.youtube.com/watch?v=LVYMwW79j6Q","_blank");''')
     time.sleep(15)
     browser.execute_script('''window.open("https://www.youtube.com/watch?v=LVYMwW79j6Q","_blank");''')
     time.sleep(15)
     browser.execute_script('''window.open("https://www.youtube.com/watch?v=LVYMwW79j6Q","_blank");''')
     time.sleep(15)
     browser.execute_script('''window.open("https://www.youtube.com/watch?v=LVYMwW79j6Q","_blank");''')
     time.sleep(15)
     browser.execute_script('''window.open("https://www.youtube.com/watch?v=LVYMwW79j6Q","_blank");''')
     time.sleep(15)
     
     print('Started')
     time.sleep(66)
     print('Done')
     driver.quit()
     time.sleep(5)

