import sys
import os

import pyautogui
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options

import time


class Crawling:

    url = "https://www.kebhana.com/"
    
    chrome_options = Options()
    chrome_options.add_extension('dncepekefegjiljlfbihljgogephdhph.crx')
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(executable_path='chromedriver',chrome_options=chrome_options)
    driver.implicitly_wait(10)


    def __init__(self,my_id,pw):
        self.my_id = my_id
        self.pw = pw

    def move_to_page(self):

        # 로그인 
        self.driver.get(url=self.url)
        self.driver.find_element_by_xpath('//*[@id="contents"]/div[2]/ul/li[1]/a/span').click()
        time.sleep(10)
        self.driver.execute_script("document.getElementsByName('userId')[0].value=\'" + self.my_id + "\'")
        self.driver.find_element_by_name('pw').click()
        time.sleep(0.5)
        pyautogui.write(self.pw,interval=0.1)
        self.driver.find_element_by_xpath('//*[@class="btn1 id-login"]').click()
        time.sleep(5)

        # 계좌 조회 페이지 이동
        self.driver.switch_to_frame("hanaMainframe")
        time.sleep(0.1)
        self.driver.find_element_by_xpath('//*[@id="diyLnb"]/ul/li[3]/a').click()     
        time.sleep(1)

