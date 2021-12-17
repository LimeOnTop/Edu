from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from .base_page import BasePage


class MarketPage(BasePage):
    URL = "https://steamcommunity.com/market/"
    ELEMENTS = {"advanced options": "//*[@id='market_search_advanced_show']/div",
                "option window": "//*[@id='market_advancedsearch_dialog']",
                "select app": "//*[@id='market_advancedsearch_appselect']",
                "dota 2": "//div[@id='market_advancedsearch_appselect_options_apps']/descendant::*[contains(text(),'Dota 2')]",
                "select hero": "//select[contains(@name, 'Hero')]",
                "rarity": "//input[@value='tag_Rarity_Immortal']",
                "search input": "//*[@id='advancedSearchBox']",
                "search": "//*[contains(@onclick, 'submit')]",
                "filters": "//*[@id='BG_bottom']/div[1]/div",
                "elements": "//div[contains(@class, 'market_listing_row')]/descendant::span[8]",
                "clear golden": "//*[contains(text(), 'golden')]/span",
                "clear dota 2": "//*[@id='BG_bottom']/div[1]/div/a[1]/span",
                "element": "//*[@id='result_0_name']",
                }

    def search_box_input(self, name, input):
        self.get_element(name).send_keys(input)

    def select_option(self, name, hero):
        Select(self.get_element(name)).select_by_visible_text(hero)

    def check_result_row(self, name, word):
        elements = self.driver.find_elements(By.XPATH, self.ELEMENTS[name])
        for i in range(5):
            if word not in elements[i].text.lower():
                return False
                break
        return True

    def list_update(self, name, word):
        element = self.driver.find_element(By.XPATH, self.ELEMENTS[name])
        if word in element.text.lower():
            return False
        else:
            return True
