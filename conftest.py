import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.home import HomePage
from constants import BASE_URL


@pytest.fixture
def driver():
    with allure.step('Открываем браузер Chrome'):
        options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=2560,1440")
    driver = webdriver.Chrome(options=options)

    yield driver

    driver.quit()


@pytest.fixture
def home_page(driver):
    with allure.step('Открываем домашнюю страницу'):
        driver.get(BASE_URL)
        home_page = HomePage(driver)
        home_page.scooter_is_visible()
        return home_page
