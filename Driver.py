import time

from selenium import webdriver


class Driver(object):
    def __init__(self, driver):
        self._driver = driver
        self._driver.implicitly_wait(10)

    def __del__(self):
        self._driver.close()

    @property
    def driver(self):
        return self._driver

    @property
    def url(self):
        return self._url

    def login(self, usr, pss, xpaths, url='https://www.doordash.com'):
        """Login function

        usr: str username
        pss: str password
        xpaths: dict {'user': <usr's xpath>, 'pass': <pss' xpath>}
        """
        self.navigate(url)

        try:
            signin_btn = self.get_element_by_xpath('//*[@id="root"]/div/div[1]/div[1]/div/div/a[1]')
            self.click_elem(signin_btn)

            email_elem = self.get_element_by_xpath(xpaths['user'])
            self.fill_in(email_elem, usr)

            psswd_elem = self.get_element_by_xpath(xpath_dict['password'])
            self.fill_in(psswd_elem, pss)

            submt_elem = self.get_element_by_xpath(xpath_dict['submit'])
            self.click_elem(submt_elem)
        except Exception as e:
            raise ValueError(e)

    def get_element_by_xpath(self, path):
        return self._driver.find_element_by_xpath(path)

    def click_elem(self, elem):
        elem.click()

    def fill_in(self, elem, string):
        elem.send_keys(string)

    def navigate(self, url):
        if url is None:
            raise ValueError(f"Url {url} is incomplete")
        self._driver.get(url)


class ChromeDriver(Driver):
    _exec = './chromedriver'

    def __init__(self, driver=None):
        if driver is None:
            caps = webdriver.DesiredCapabilities.CHROME.copy()
            caps['acceptInsecureCerts'] = True
            driver = webdriver.Chrome(self._exec, desired_capabilities=caps)

        super(ChromeDriver, self).__init__(driver)


if __name__ == '__main__':
    xpath_dict = {'user': '//*[@id="FieldWrapper-2"]',
                  'password': '//*[@id="FieldWrapper-3"]',
                  'submit': '//*[@id="login-submit-button"]'}

    user = 'X'
    pssw = 'Y'

    dvr = ChromeDriver()
    try:
        dvr.login(user, pssw, xpath_dict)
        time.sleep(50)
    except Exception as e:
        print(e)
    finally:
        del dvr
