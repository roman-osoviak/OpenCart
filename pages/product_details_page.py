"""
This module describes Product's Details Page
"""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.common import trim_currency_from_string


# pylint: disable=too-few-public-methods
class ProductDetailsLocators:
    """Locator on Product's Details Page"""
    ADD_TO_WISH_LIST_BUTTON = (
        By.XPATH, '//h1/..//*[@aria-label="Add to Wish List"]')
    ADD_TO_COMPARE_BUTTON = (By.XPATH, '//h1/..//*[@aria-label="Compare this Product"]')
    BRAND_APPLE_LINK = (By.XPATH, '//li[contains(text(), "Brand: ")]//a[text()="Apple"]')
    OLD_PRICE = (By.XPATH, '//*[@class="price-old"]')
    NEW_PRICE = (By.XPATH, '//*[@class="price-new"]')
    MUST_TO_LOGIN_WISH_LIST = ''


class ProductDetailsPage(BasePage):
    """Class for Product's Details Page"""
    _URL_PATH = '?route=product/product&language=en-gb&product_id=42'

    def go_to_site(self):
        """Open details page"""
        return self.driver.get(self.base_url + self._URL_PATH)

    def click_on_add_wish_button(self):
        """Method that clicks on Wish btn"""
        self.click_on_element(ProductDetailsLocators.ADD_TO_WISH_LIST_BUTTON)

    def click_on_add_compare_list(self):
        """Method that clicks on add to compare list"""
        self.click_on_element(ProductDetailsLocators.ADD_TO_COMPARE_BUTTON)

    def click_on_brand(self):
        """Method clicks on Apple brand link"""
        self.click_on_element(ProductDetailsLocators.BRAND_APPLE_LINK)

    def verify_new_price_is_greater_than_old(self):
        """
        Verifying that new price is lower than new one

        :return: True, otherwise False
        """
        new_price_is_greater = False
        if (float(trim_currency_from_string
                      (self.get_element_text(ProductDetailsLocators.OLD_PRICE)))
            - float(trim_currency_from_string
                        (self.get_element_text(ProductDetailsLocators.NEW_PRICE))
                    )) > 0:
            new_price_is_greater = True
        return new_price_is_greater
