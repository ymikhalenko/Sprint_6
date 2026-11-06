import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base import BasePage
from locators.order_locators import OrderPageLocators


class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Ввести имя")
    def input_first_name(self, text):
        self.input(OrderPageLocators.first_name_input, text)

    @allure.step("Ввести фамилию")
    def input_last_name(self, text):
        self.input(OrderPageLocators.last_name_input, text)

    @allure.step("Ввести адрес")
    def input_address(self, text):
        self.input(OrderPageLocators.address_input, text)

    @allure.step("Ввести станцию метро")
    def input_subway_station(self, text):
        self.input(OrderPageLocators.subway_station_input, text)

    @allure.step("Выбрать станцию метро в выпадающем списке")
    def click_subway_station(self, text):
        locator = (
            By.XPATH, OrderPageLocators.subway_station_dropdown_option.format(text=text))
        self.click(locator)
        self.wait.until(
            EC.invisibility_of_element_located(OrderPageLocators.subway_station_dropdown))

    @allure.step("Ввести номер телефона")
    def input_phone(self, text):
        self.input(OrderPageLocators.phone_input, text)

    @allure.step("Нажать кнопку 'Далее'")
    def click_proceed_button(self):
        self.click(OrderPageLocators.proceed_button)

    @allure.step("Ввести дату")
    def input_date(self, text):
        self.input(OrderPageLocators.date_input, text)
        self.press_enter(OrderPageLocators.date_input)

    @allure.step("Нажать на поле 'Срок аренды'")
    def click_period_input(self):
        self.click(OrderPageLocators.period_dropdown)
        self.wait.until(EC.presence_of_element_located(
            OrderPageLocators.period_dropdown))

    @allure.step("Выбрать срок аренды")
    def select_period(self, days: int):
        match days:
            case 1:
                self.click(OrderPageLocators.period_dropdown_option_1_day)
            case 2:
                self.click(OrderPageLocators.period_dropdown_option_2_days)

    @allure.step("Выбрать черный цвет")
    def select_black_color(self):
        self.click(OrderPageLocators.color_black)

    @allure.step("Выбрать серый цвет")
    def select_gray_color(self):
        self.click(OrderPageLocators.color_grey)

    @allure.step("Ввести комментарий")
    def input_comment(self, text):
        self.input(OrderPageLocators.comment_input, text)

    @allure.step("Нажать кнопку 'Заказать'")
    def click_submit_button(self):
        self.click(OrderPageLocators.submit_button)

    @allure.step("Нажать кнопку 'Да'")
    def click_confirm_button(self):
        self.click(OrderPageLocators.confirm_button)
