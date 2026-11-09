import time
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from locators.base_locators import BasePageLocators
from constants import GET_WEB_ELEMENT_TIMEOUT


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = GET_WEB_ELEMENT_TIMEOUT
        self.wait = WebDriverWait(driver, self.timeout)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def get_current_url(self):
        return self.driver.current_url

    def is_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.click()

    def input(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)

    def press_enter(self, locator):
        element = self.find_element(locator)
        element.send_keys(Keys.ENTER)

    def scroll(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element)

    def switch_to_new_window(self):
        self.wait.until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.wait.until(EC.url_changes("about:blank"))

    def save_screenshot(self, filename):
        self.driver.save_screenshot(filename)

    @allure.step("Нажать на кнопку 'Заказать' в хэдере")
    def click_header_order_button(self):
        self.click(BasePageLocators.header_order_button)

    @allure.step("Нажать на логотим 'Самокат' в хэдере")
    def click_header_scooter_logo(self):
        self.click(BasePageLocators.header_scooter_logo)

    @allure.step("Нажать на логотим 'Яндекс' в хэдере")
    def click_header_yandex_logo(self):
        self.click(BasePageLocators.header_yandex_logo)
