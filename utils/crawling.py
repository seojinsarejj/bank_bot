import sys
import os

import pyautogui
import selenium
from selenium import webdriver

from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup

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


    def inquire_transaction(self,period,amount):

        self.move_to_page()
        # period = 1:당일, 2:3일, 3:1주, 4:2주, 5:1개월, 6:3개월, 7:6개월, 8:1년
        self.driver.find_element_by_xpath('//*[@id="transactForm"]/table/tbody/tr[3]/td/ul/span[{}]/a'.format(period)).click()
        time.sleep(0.1)
        # amount = 15, 30, 50, 100
        self.driver.find_element_by_xpath('//label[@for="listSize{}"]'.format(amount)).click()
        time.sleep(0.3)
        self.driver.find_element_by_xpath('//*[@id="searchBtn"]/span').click()
        time.sleep(1)
        return self.driver.page_source