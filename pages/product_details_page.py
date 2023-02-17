"""
This module describes Product's Details Page
"""

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.common import trim_currency_from_string, get_random_string
from utils.enums import ProductDetailsPageRadio


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

    # radio
    # pylint: disable=unnecessary-lambda-assignment
    RADIO_BUTTON = lambda text: (By.XPATH, f'//label[contains(text(), "{text}")]//..//input')
    RADIO_OPTIONS_LABELS = lambda text: \
        (By.XPATH, f'//label[contains(normalize-space(text()), "{text}")]')
    RADIO_LABEL_SMALL = (By.XPATH, '//label[contains(normalize-space(text()), "Small")]')
    RADIO_OPTION_MEDIUM = (By.XPATH, '//label[contains(normalize-space(text()), "Medium")]')
    RADIO_OPTION_LARGE = (By.XPATH, '//label[contains(normalize-space(text()), "Large")]')
    # checkbox
    CHECKBOX_BUTTONS = (By.XPATH, '//label[text()="Checkbox"]//..//input')
    CHECKBOX_BUTTON_FIRST = (By.XPATH, '//label[contains(text(), "Checkbox 1")]//../input')
    CHECKBOX_BUTTON_SECOND = (By.XPATH, '//label[contains(text(), "Checkbox 2")]//../input')
    CHECKBOX_BUTTON_THIRD = (By.XPATH, '//label[contains(text(), "Checkbox 3")]//../input')
    CHECKBOX_BUTTON_FOURTH = (By.XPATH, '//label[contains(text(), "Checkbox 4")]//../input')
    CHECKBOX_LABEL_FIRST = (By.XPATH,
                            '//label[contains(normalize-space(text()), "Checkbox 1 (+$14.00)")]')
    CHECKBOX_LABEL_SECOND = (By.XPATH,
                             '//label[contains(normalize-space(text()), "Checkbox 2 (+$26.00)")]')
    CHECKBOX_LABEL_THIRD = (By.XPATH,
                            '//label[contains(normalize-space(text()), "Checkbox 3 (+$38.00)")]')
    CHECKBOX_LABEL_FOURTH = (By.XPATH,
                             '//label[contains(normalize-space(text()), "Checkbox 4 (+$50.00)")]')

    # text
    TEXT_INPUT = (By.XPATH, '//input[@placeholder="Text"]')


class ProductDetailsAttributes:
    """Class describes attribute names"""
    ATTRIBUTE_PLACEHOLDER = 'placeholder'
    ATTRIBUTE_VALUE = 'value'
    ATTRIBUTE_TEXT = 'text'


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

    def click_on_text_field(self):
        """
        Clicking on text field

        :return: None
        """
        self.find_element(ProductDetailsLocators.TEXT_INPUT).click()

    def verify_old_price_is_greater_than_new(self):
        """
        Verifying that new price is lower than old one

        :return: True, otherwise False
        """
        old_price = float(trim_currency_from_string(
            self.get_element_text(ProductDetailsLocators.OLD_PRICE)))
        new_price = float(trim_currency_from_string(
            self.get_element_text(ProductDetailsLocators.NEW_PRICE)))
        return old_price > new_price

    def get_alert_text(self):
        """
        Method returns alert's text value

        :return: alert's text
        """

        return self.get_element_text(ProductDetailsLocators.TOP_ALERT)

    def get_text_input_text(self):
        """
        Method that retrieve input field text

        :return: input's text
        """
        return self.get_element_text(ProductDetailsLocators.TEXT_INPUT)

    # def get_attribute_value(self):
    #     """
    #     Method that returns placeholder attribute
    #
    #     :return: placeholder text
    #     """
    #     # return self.get_element_attribute(ProductDetailsLocators.TEXT_INPUT,
    #     #                                   ProductDetailsAttributes.ATTRIBUTE_VALUE)

    def get_text_attribute_value(self, radio_btn_option: ProductDetailsPageRadio):
        """
        Method that returns text from element

        :param radio_btn_option:
        :return:
        """
        return self.get_element_text(
            ProductDetailsLocators.RADIO_OPTIONS_LABELS(radio_btn_option.value))

    def verify_alert_is_displayed(self, is_displayed: bool = True):
        """
        Check if our alert element is shown

        :return: True if success, otherwise None
        """
        if is_displayed:
            assert self.is_element_displayed(ProductDetailsLocators.MUST_TO_LOGIN_WISH_LIST)
        else:
            assert self.is_element_invisible(ProductDetailsLocators.MUST_TO_LOGIN_WISH_LIST)

    def set_random_string_to_text_input(self):
        """
        Generate and input random string into text field

        :return: None
        """
        self.type_text_in_ui_element(ProductDetailsLocators.TEXT_INPUT, get_random_string(4))

    def click_on_radio_button(self, radio_btn_option: ProductDetailsPageRadio):
        """
        Method that selects desired radio-button

        :return: None
        """
        self.find_element(ProductDetailsLocators.RADIO_BUTTON(radio_btn_option.value)).click()
        return self

    def verify_radio_button_is_selected(self, radio_btn_option: ProductDetailsPageRadio,
                                        is_selected: bool = True) -> object:
        """
        Method that checks if radio button is selected

        :return: True if selected, False otherwise
        """
        if is_selected:
            self.is_element_selected(ProductDetailsLocators.RADIO_BUTTON(radio_btn_option.value))
        else:
            self.is_element_not_selected(
                ProductDetailsLocators.RADIO_BUTTON(radio_btn_option.value))
        return self
