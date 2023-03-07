"""Module consists of locators for Store Page"""
from selenium.webdriver.common.by import By


# pylint: disable=too-few-public-methods
class StoreLocators:
    """Locators on Your Store page"""
    SHOPPING_CART_BUTTON = (By.XPATH, '//div[@id="header-cart"]//button')
    NEXT_ITEM_BUTTON = (By.XPATH, '//*[@id="carousel-banner-0"]//span')
    PREVIOUS_ITEM_BUTTON = (By.XPATH, '//*[@id="carousel-banner-0"]//span')
    SHOPPING_CART_DROPDOWN_MENU_EXPANDED = (By.XPATH,
                                            '//div[@id="header-cart"]//p[@class="text-center"]')
    CURRENCY_SIGN_USD = (By.XPATH, '//*[@id="form-currency"]//strong[starts-with(text(), "$")]')
    CURRENCY_SIGN = (By.XPATH, '//*[@id="form-currency"]//strong')
    CURRENCY_DROP_DOWN = (By.XPATH, '//*[@id="form-currency"]//span')
    CURRENCY_OPTION_EURO = (By.XPATH, '//*[contains(text(), "Euro")]')
    CURRENCY_OPTION_POUNDS = (By.XPATH, '//*[contains(text(), "Pound Sterling")]')
    CURRENCY_OPTION_USD = (By.XPATH, '//*[contains(text(), "US Dollar")]')
