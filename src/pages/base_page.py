from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    ELEMENTS = {}
    URL = ""

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def get_element(self, name):
        return self.driver.find_element(By.XPATH, self.ELEMENTS[name])

    def click_on_the_link(self, name):
        self.get_element(name).click()
