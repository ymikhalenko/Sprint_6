from selenium.webdriver.common.by import By


class BasePageLocators:
    header = "//div[contains(@class, 'Header_Header')]"
    header_yandex_logo = (
        By.XPATH, f"{header}//a[contains(@class, 'Header_LogoYandex')]")
    header_scooter_logo = (
        By.XPATH, f"{header}//a[contains(@class, 'Header_LogoScooter')]")
    header_order_button = (
        By.XPATH, f"{header}//button[contains(@class, 'Button_Button') and contains(text(), 'Заказать')]")
