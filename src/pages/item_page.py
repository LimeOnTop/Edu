from .base_page import BasePage
from selenium import webdriver


class ItemPage(BasePage):
    URL = "https://store.steampowered.com"
    ELEMENTS = {
        "item name": "//*[@id='largeiteminfo_item_name']"
    }
