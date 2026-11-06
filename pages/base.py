import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
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
        element = self.wait.until(EC.presence_of_element_located(locator))
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
            "arguments[0].scrollIntoView(true);", element)

    def switch_to_new_window(self):
        self.wait.until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def save_screenshot(self, filename):
        self.driver.save_screenshot(filename)

    @allure.step("Нажать на кнопку 'Заказать' в хэдере")
    def click_header_order_button(self):
        from pages.order import OrderPage
        self.click(BasePageLocators.header_order_button)
        return OrderPage(self.driver)

    @allure.step("Нажать на логотим 'Самокат' в хэдере")
    def click_header_scooter_logo(self):
        from pages.home import HomePage
        self.click(BasePageLocators.header_scooter_logo)
        return HomePage(self.driver)

    @allure.step("Нажать на логотим 'Яндекс' в хэдере")
    def click_header_yandex_logo(self):
        self.click(BasePageLocators.header_yandex_logo)
