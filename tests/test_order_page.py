import pytest
import allure
from constants import BASE_URL, YANDEX_URL
from pages.order_page import OrderPage

test_cases = [
    ('click_main_order_button', 'Иван', 'Иванов',
     'ул. Бассейная', 'Спортивная', '+79999999999', '12.12.26', 1, 'select_black_color', 'urent'),
    ('click_header_order_button', 'Петр', 'Пиванов',
     'ул. Джакузи', 'Черкизовская', '89999999999', '13.12.26', 2, 'select_gray_color', 'SALE20'),
]


@allure.title("Позитивный флоу создания заказа")
@pytest.mark.parametrize("click_button_method, first_name, last_name, address, subway_station, phone, date, period, select_color_method, comment", test_cases)
def test_order_positive_flow(home_page, click_button_method, first_name, last_name, address, subway_station, phone, date, period, select_color_method, comment):
    resolved_click_button_method = getattr(home_page, click_button_method)
    resolved_click_button_method()
    order_page = OrderPage(home_page.driver)
    order_page.input_first_name(first_name)
    order_page.input_last_name(last_name)
    order_page.input_address(address)
    order_page.input_subway_station(subway_station)
    order_page.click_subway_station(subway_station)
    order_page.input_phone(phone)
    order_page.click_proceed_button()
    order_page.input_date(date)
    order_page.click_period_input()
    order_page.select_period(period)
    resolved_select_color_method = getattr(order_page, select_color_method)
    resolved_select_color_method()
    order_page.input_comment(comment)
    order_page.click_submit_button()
    order_page.click_confirm_button()
    assert order_page.is_order_success_message_visible()


@allure.title("Переход по иконке 'Самокаты'")
def test_scooter_logo_redirection(home_page):
    home_page.click_header_scooter_logo()
    assert home_page.get_current_url() == BASE_URL


@allure.title("Переход по иконке 'Яндекс'")
def test_yandex_logo_redirection(home_page):
    home_page.click_header_yandex_logo()
    home_page.switch_to_new_window()
    assert YANDEX_URL in home_page.get_current_url()
