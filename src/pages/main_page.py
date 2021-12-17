from .base_page import BasePage
from selenium import webdriver


class MainPage(BasePage):
    URL = "https://store.steampowered.com"
    ELEMENTS = {"about": "//div[@class='supernav_container']/a[3]","community": "//div[@class='supernav_container']/a[2]", "market": "//*[@id='global_header']/div/div[2]/div[2]/div/a[4]"}

    def move_to_the_link(self,name):
        webdriver.ActionChains(self.driver).move_to_element(self.get_element(name)).perform()
