from selenium.webdriver.common.by import By


class OrderPageLocators:
    order_contact_title = (
        By.XPATH, "//div[contains(@class, 'Order_Header') and contains(text(), 'Для кого самокат')]")
    first_name_input = (
        By.XPATH, "//input[contains(@class, 'Input_Input') and contains(@placeholder, '* Имя')]")
    last_name_input = (
        By.XPATH, "//input[contains(@class, 'Input_Input') and contains(@placeholder, '* Фамилия')]")
    address_input = (
        By.XPATH, "//input[contains(@class, 'Input_Input') and contains(@placeholder, '* Адрес: куда привезти заказ')]")
    subway_station_input = (
        By.XPATH, "//input[contains(@class, 'select-search__input') and contains(@placeholder, '* Станция метро')]")
    subway_station_dropdown = (
        By.XPATH, "//div[contains(@class, 'select-search__select')]")
    subway_station_dropdown_option = "//button[contains(@class, 'select-search__option') and contains(., '{text}')]"
    phone_input = (
        By.XPATH, "//input[contains(@class, 'Input_Input') and contains(@placeholder, '* Телефон: на него позвонит курьер')]")
    proceed_button = (
        By.XPATH, "//button[contains(@class, 'Button_Button') and contains(text(), 'Далее')]")
    order_rent_title = (
        By.XPATH, "//div[contains(@class, 'Order_Header') and contains(text(), 'Про аренду')]")
    date_input = (
        By.XPATH, "//input[contains(@class, 'Input_Input') and contains(@placeholder, '* Когда привезти самокат')]")
    period_dropdown = (
        By.XPATH, "//div[contains(@class, 'Dropdown-placeholder') and contains(text(), '* Срок аренды')]")
    period_dropdown_option = "//div[contains(@class, 'Dropdown-option') and contains(., '{text}')]"
    period_dropdown_option_1_day = (
        By.XPATH, period_dropdown_option.format(text="сутки"))
    period_dropdown_option_2_days = (
        By.XPATH, period_dropdown_option.format(text="двое суток"))
    color_black = (
        By.XPATH, "//input[contains(@class, 'Checkbox_Input') and contains(@id, 'black')]")
    color_grey = (
        By.XPATH, "//input[contains(@class, 'Checkbox_Input') and contains(@id, 'grey')]")
    comment_input = (
        By.XPATH, "//input[contains(@class, 'Input_Input') and contains(@placeholder, 'Комментарий для курьера')]")
    submit_button = (
        By.XPATH, "//div[contains(@class, 'Order_Content')]//button[contains(@class, 'Button_Button') and contains(text(), 'Заказать')]")
    # Используется кнопка "Нет" вместо "Да", т.к. сейчас в тренажере не работает кнопка "Да"
    confirm_button = (
        By.XPATH, "//div[contains(@class, 'Order_Modal')]//button[contains(@class, 'Button_Button') and contains(text(), 'Нет')]")
