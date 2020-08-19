import os
import configparser
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


CONFIG = './conf.ini'
URL = 'https://www.doordash.com'
EMAIL_FORM_ELEMENT_ID = 'FieldWrapper-2'
PASSWD_FORM_ELEMENT_ID = 'FieldWrapper-3'
SUBMIT_FORM_ELEMENT_ID = 'login-submit-button'

def signin(driver):
    driver.get(URL)
    print(driver.title)

    # redirect to login page
    signin_btn = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[1]/div/div/a[1]')
    signin_btn.click()

    # extract login input form and fill it out
    email = driver.find_element_by_id(EMAIL_FORM_ELEMENT_ID)
    pwd = driver.find_element_by_id(PASSWD_FORM_ELEMENT_ID)
    submit = driver.find_element_by_id(SUBMIT_FORM_ELEMENT_ID)

    email.clear()
    pwd.clear()
    email.send_keys(os.environ['DD_USER'])
    pwd.send_keys(os.environ['DD_PASSWORD'])
    time.sleep(2)
    submit.click()


def webdriver_setup(driver='./chromedriver'):
    return webdriver.Chrome(driver)


def config_setup():
    config = configparser.ConfigParser()
    config.read(CONFIG)

    if 'DD_USER' not in os.environ:
        os.environ['DD_USER'] = config['doordash.com']['DD_USER']
    if 'DD_PASSWORD' not in os.environ:
        os.environ['DD_PASSWORD'] = config['doordash.com']['DD_PASSWORD']


def main():
    config_setup()
    driver = webdriver_setup()

    # setup implicit waits to poll dom for certain amount of time (10 s)
    driver.implicitly_wait(10)
    signin(driver)

    #time.sleep(5)
    driver.close()


if __name__ == "__main__":
    main()

