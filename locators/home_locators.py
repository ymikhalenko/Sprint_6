from selenium.webdriver.common.by import By


class HomePageLocators:
    order_button = (
        By.XPATH, "//div[contains(@class, 'Home_RoadMap')]//button[(contains(@class, 'Button_Middle') or contains(@class, 'Button_UltraBig')) and contains(text(), 'Заказать')]")
    scooter_blueprint_image = (
        By.XPATH, "//div[contains(@class, 'Home_BluePrint')]")
    accordion_button = "//div[contains(@class, 'accordion__button') and contains(text(), '{text}')]"
    accordion_panel = "//div[div[div[contains(@class, 'accordion__button') and contains(text(), '{text}')]]]//div[contains(@class, 'accordion__panel')]/p"
