import sys
import os

import pyautogui
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.chrome.options import Options

import time


class Crawling:

    url = "https://www.kebhana.com/common/login.do#//HanaBank"

    chrome_options = Options()
    chrome_options.add_extension('dncepekefegjiljlfbihljgogephdhph.crx')
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(executable_path='chromedriver',chrome_options=chrome_options)
    
    def login(self,my_id,pw):

        self.driver.get(url=self.url)
        self.driver.execute_script("document.getElementsByName('userId')[0].value=\'" + my_id + "\'")
        time.sleep(0.5)
        self.driver.find_element_by_name('pw').click()
        time.sleep(0.5)
        pyautogui.write(pw,interval=0.1)
        self.driver.find_element_by_xpath('//*[@class="btn1 id-login"]').click()
        time.sleep(1)
    


        