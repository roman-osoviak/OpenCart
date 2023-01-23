"""
This module describes Your Store Page
"""
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


# pylint: disable=too-few-public-methods
class StoreLocators:
    """Locators on Your Store page"""
    SHOPPING_CART_BUTTON = (By.XPATH, '//*[@id="header-cart"]/div/button')
    NEXT_ITEM_BUTTON = (By.XPATH, '//*[@id="carousel-banner-0"]/button[2]/span')
    PREVIOUS_ITEM_BUTTON = (By.XPATH, '//*[@id="carousel-banner-0"]/button[1]/span')
    SHOPPING_CART_DROPDOWN_MENU_EXPANDED = (By.XPATH, '//*[@id="header-cart"]')


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
