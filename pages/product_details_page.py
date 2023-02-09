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
    TOP_ALERT = (By.XPATH, '//div[@id="alert"]')
    MUST_TO_LOGIN_WISH_LIST = (By.XPATH, '//div[@id="alert"]/div[contains(@class, "alert")]')


class ProductDetailsPage(BasePage):
    """Class for Product's Details Page"""
    _URL_PATH = '?route=product/product&language=en-gb&product_id=42'

    def go_to_site(self):
        """Open details page"""
        return self.driver.get(self.base_url + self._URL_PATH)

    def click_on_add_wish_button(self):
        """Method that clicks on Wish btn"""
        self.click_on_element(ProductDetailsLocators.ADD_TO_WISH_LIST_BUTTON)

    def click_on_add_compare_button(self):
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

    def get_alert_text(self):
        """
        Method returns alert's text value

        :return: alert's text
        """
        return self.get_element_text(ProductDetailsLocators.TOP_ALERT)

    def verify_alert_is_displayed(self, is_displayed: bool = True):
        """
        Check if our alert element is shown

        :return: True if success, otherwise None
        """
        if is_displayed:
            assert self.is_element_displayed(ProductDetailsLocators.MUST_TO_LOGIN_WISH_LIST)
        else:
            # assert not self.is_element_displayed(ProductDetailsLocators.MUST_TO_LOGIN_WISH_LIST)
            assert self.is_element_invisible(ProductDetailsLocators.MUST_TO_LOGIN_WISH_LIST)
