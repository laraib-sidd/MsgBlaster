from selenium import webdriver

import time
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import os
import xlrd

# loc = ("UserNames.xls")

# wb = xlrd.open_workbook(loc)
# sheet = wb.sheet_by_index(0)

# # For row 0 and column 0
# sheet.cell_value(0, 0)
# names = []
# for i in range(123):
#     print(sheet.cell_value(i, 0))
#     names.append(sheet.cell_value(i, 0))
# print(names)

from webdriver_manager.chrome import ChromeDriverManager


def scraper(names):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)

    #driver = webdriver.Chrome("/usr/local/bin/chromedriver", options = chrome_options)
    driver.get('https://instagram.com')
    time.sleep(6)
    element = driver.find_element_by_xpath(
        '//*[@id="loginForm"]/div/div[1]/div/label/input')

    element.send_keys('threshold.babson2024')

    element = driver.find_element_by_name('password')

    element.send_keys('babson2024')

    element = driver.find_element_by_xpath(
        '//*[@id="loginForm"]/div/div[3]/button').click()
    time.sleep(4)
    element = driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/div/div/div/button').click()
    time.sleep(4)
    element = driver.find_element_by_xpath(
        '/html/body/div[4]/div/div/div/div[3]/button[2]').click()
    time.sleep(2)
    driver.get('https://www.instagram.com/direct/inbox/')
    time.sleep(6)
    #names = []
    # z = 0
    for name in names:
        element = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()
        time.sleep(10)
        element = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(
            name)
        time.sleep(10)
        element = driver.find_element_by_xpath(
            '/html/body/div[5]/div/div/div[2]/div[2]/div[1]/div/div[3]/button').click()
        time.sleep(10)
        element = driver.find_element_by_xpath(
            '/html/body/div[5]/div/div/div[1]/div/div[2]/div/button').click()
        time.sleep(10)
        time.sleep(10)

        element = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(
            'Snapchat Promo!')
        ActionChains(driver).key_down(Keys.SHIFT).key_down(
            Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
        ActionChains(driver).key_down(Keys.SHIFT).key_down(
            Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
        element = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys('Hey! Do you have a snapchat account?')
        ActionChains(driver).key_down(Keys.SHIFT).key_down(
            Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
        ActionChains(driver).key_down(Keys.SHIFT).key_down(
            Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
        element = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(
            'We have a potential opportunity for you if so!')

        time.sleep(10)
        element = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()

    # z += 1
    # if z == 10:
    #     time.sleep(60)

    driver.close()
scraper(['laraib'])