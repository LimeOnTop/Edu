from selenium.webdriver.common.by import By
from .base_page import BasePage


class AboutPage(BasePage):
    URL = "https://store.steampowered.com/about/"
    ELEMENTS = {"online": "//*[@id='about_greeting']/div[3]/div[1]",
                "in game": "//*[@id='about_greeting']/div[3]/div[2]"}

    def check_people_count(self, name_1, name_2):
        online = self.get_element(name_1).text
        online = online[6:].replace(",","")
        in_game = self.get_element(name_2).text
        in_game = in_game[6:].replace(",","")
        return int(online) > int(in_game)
