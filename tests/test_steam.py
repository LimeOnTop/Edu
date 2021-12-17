from selenium import webdriver
from pytest import fixture
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from src.pages.main_page import MainPage
from src.pages.about_page import AboutPage
from src.pages.market_page import MarketPage
from src.pages.item_page import ItemPage
from src.config.config import CONFIG


# используем фикстуру с параметром сессии для создания Singleton
@fixture(scope="session")
def driver():
    return webdriver.Chrome(ChromeDriverManager().install())


# используем фикстуру для настройки браузера
@fixture(scope="session")
def browser_config(driver: WebDriver):
    driver.set_window_rect(CONFIG["pos x"], CONFIG["pos y"], CONFIG["browser width"], CONFIG["browser height"])
    yield
    driver.close()


def test_1(driver: WebDriver, browser_config):
    # обьявляем необходимые классы
    main_page = MainPage(driver)
    about_page = AboutPage(driver)

    # используем функцию класса для открытия страницы
    main_page.open()

    # проверяем что открыта главная страница
    page_url = driver.current_url
    assert (page_url, main_page.URL)

    # нажимаем на искомую ссылку
    main_page.click_on_the_link("about")

    # проверяем что мы перешли на нужную страницу
    page_url = driver.current_url
    assert (page_url, about_page.URL)

    # функция check_people_count возвращает true если счетчик "в сети" больше счетчика "в игре".
    assert about_page.check_people_count("online", "in game")

    # возвращаемся на страницу магазина и делаем проверку
    main_page.open()
    page_url = driver.current_url
    assert (page_url, main_page.URL)


def test_2(driver: WebDriver, browser_config):
    # обьявляем необходимые классы
    main_page = MainPage(driver)
    market_page = MarketPage(driver)
    item_page = ItemPage(driver)

    # используем функцию класса для открытия страницы
    main_page.open()

    # проверяем что открыта главная страница
    page_url = driver.current_url
    assert (page_url, main_page.URL)

    # переносим курсор мыши на вкладку сообщество
    main_page.move_to_the_link("community")

    # нажимаем на искомую ссылку
    main_page.click_on_the_link("market")

    # проверяем что открыта главная страница
    page_url = driver.current_url
    assert (page_url, market_page.URL)

    # открываем расширенные настройки
    market_page.click_on_the_link("advanced options")

    # проверяем что настройки отобразились
    assert market_page.get_element("option window").is_displayed()

    # выбираем необходимые фильтры
    market_page.click_on_the_link("select app")
    market_page.click_on_the_link(CONFIG["game"])
    driver.implicitly_wait(10)
    market_page.select_option("select hero", CONFIG["hero"])
    market_page.click_on_the_link("rarity")
    market_page.search_box_input("search input", CONFIG["word"])
    market_page.click_on_the_link("search")

    # проверяем что фильтры отображаются
    assert market_page.get_element("filters").is_displayed()

    # проверяем результат на примененные фильтры
    assert market_page.check_result_row("elements", CONFIG["word"])

    # удаляем необходимые фильтры
    market_page.click_on_the_link(CONFIG["clear filter 1"])
    market_page.click_on_the_link(CONFIG["clear filter 2"])

    # проверяем что список обновился
    assert market_page.list_update("element", CONFIG["word"])

    # переходим на страницу предмета и делаем проверку по названию
    item = market_page.get_element("element").text
    market_page.click_on_the_link("element")
    current_item_name = item_page.get_element("item name").text
    assert (item, current_item_name)
