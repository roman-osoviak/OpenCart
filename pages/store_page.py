"""
This module describes Your Store Page
"""
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.enums import Currency


# pylint: disable=too-few-public-methods
class StoreLocators:
    """Locators on Your Store page"""
    SHOPPING_CART_BUTTON = (By.XPATH, '//div[@id="header-cart"]//button')
    NEXT_ITEM_BUTTON = (By.XPATH, '//*[@id="carousel-banner-0"]//span')
    PREVIOUS_ITEM_BUTTON = (By.XPATH, '//*[@id="carousel-banner-0"]//span')
    SHOPPING_CART_DROPDOWN_MENU_EXPANDED = (By.XPATH,
                                            '//div[@id="header-cart"]//p[@class="text-center"]')
    CURRENCY_DROP_DOWN = (By.XPATH, '//*[@id="form-currency"]//span')
    CURRENCY_OPTION_EURO = (By.XPATH, '//*[contains(text(), "Euro"")]')
    CURRENCY_OPTION_POUNDS = (By.XPATH, '//*[contains(text(), "Pound Sterling")]')
    CURRENCY_OPTION_USD = (By.XPATH, '//*[contains(text(), "US Dollar")]')


class StorePage(BasePage):
    """Class for Your Store page"""
    _URL_PATH = '?route=common/home&language=en-gb'

    def go_to_site(self):
        """Open store page method"""
        return self.driver.get(self.base_url + self._URL_PATH)

    def click_on_next_button(self):
        """Method that clicks on Next item button"""
        self.click_on_element(StoreLocators.NEXT_ITEM_BUTTON)

    def click_on_previous_button(self):
        """Method that clicks on Previous item button"""
        self.click_on_element(StoreLocators.PREVIOUS_ITEM_BUTTON)

    def click_on_shopping_cart(self):
        """Method that clicks on Shopping cart"""
        self.click_on_element(StoreLocators.SHOPPING_CART_BUTTON)

    def click_on_drop_down_currency(self):
        """Method click on currency drop-down"""
        self.click_on_element(StoreLocators.CURRENCY_DROP_DOWN)

    def empty_shopping_cart_menu_displayed(self):
        """Checks if empty menu dropdown menu is displayed"""
        is_shown = False
        try:
            element = self.find_element(StoreLocators.SHOPPING_CART_DROPDOWN_MENU_EXPANDED)
            if element.is_displayed():
                is_shown = True
        except NoSuchElementException:
            print('No such element on the page')
        return is_shown

    def get_shopping_cart_default_button_text(self):
        """
        Gets default text from shopping cart button

        :return: element text
        """
        return self.get_element_text(StoreLocators.SHOPPING_CART_BUTTON)

    def get_shopping_cart_empty_text(self):
        """
        Get empty cart dropdown text method

        :return: text
        """
        # we need to expand dropdown before reading text
        self.click_on_shopping_cart()
        return self.get_element_text(StoreLocators.SHOPPING_CART_DROPDOWN_MENU_EXPANDED)

    def click_on_currency_option(self, currency: Currency):
        """Method click on currency option"""
        # locator = ''
        if currency == Currency.USD:
            locator = StoreLocators.CURRENCY_OPTION_USD
        elif currency == Currency.EURO:
            locator = StoreLocators.CURRENCY_OPTION_EURO
        elif currency == Currency.POUNDS:
            locator = StoreLocators.CURRENCY_OPTION_POUNDS
        self.click_on_element(locator)

    def select_currency(self, currency: str = Currency.USD):
        """
        Method for selecting desired currency

        :param currency: desired currency
        :return: None
        """
        self.click_on_drop_down_currency()
        self.click_on_currency_option(currency)
