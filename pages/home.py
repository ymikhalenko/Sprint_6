import allure
from selenium.webdriver.common.by import By
from locators.home_locators import HomePageLocators
from pages.base import BasePage
from pages.order import OrderPage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Проверить видимость скутера")
    def scooter_is_visible(self):
        return self.is_visible(HomePageLocators.scooter_blueprint_image)

    @allure.step("Нажать кнопку 'Заказать' на главной странице")
    def click_main_order_button(self):
        self.scroll(HomePageLocators.order_button)
        self.click(HomePageLocators.order_button)
        return OrderPage(self.driver)

    @allure.step("Нажать Q&A вопрос на главной странице")
    def click_qna_with_text(self, question_text: str):
        formatted_locator = (By.XPATH, HomePageLocators.accordion_button.format(
            text=question_text))
        self.scroll(formatted_locator)
        self.click(formatted_locator)

    @allure.step("Проверить Q&A ответ на главной странице")
    def qna_answer(self, question_text: str):
        formatted_locator = (By.XPATH, HomePageLocators.accordion_panel.format(
            text=question_text))
        self.scroll(formatted_locator)
        return self.is_visible(formatted_locator).text
