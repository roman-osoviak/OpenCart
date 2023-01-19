"""
This module describes Login Page
LoginPage is inherited from BasePage
"""
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


# pylint: disable=too-few-public-methods
class ForgotPasswordPageLocators:
    """Locators for Forgotten Password page"""
    EMAIL_ADDRESS_INPUT = (By.XPATH, '//*[@name="email"]')
    BACK_BUTTON = (By.XPATH, '//*[contains(text(), "Back")]')
    CONTINUE_BUTTON = (By.XPATH, '//*[@type="submit"]')
    WARNING_NOT_FOUND_RECORD = (By.XPATH, '//*[@id="alert"]/div')


class ForgotPasswordPage(BasePage):
    """This class collects methods for Forgot Password Page"""
    _URL_PATH = '?route=account/forgotten&language=en-gb'

    def go_to_site(self):
        """Open Forgot Password Page"""
        return self.driver.get(self.base_url + self._URL_PATH)

    def forgot_password(self, email: str = ''):
        """
        Forgot password flow method

        :param email: Customer Email is empty string by default
        :return: None
        """
        self.set_email(email)
        self.click_continue_button()

    def set_email(self, email: str):
        """
        Input email address method

        :param email: Customer Email
        :return: None
        """
        self.type_text_in_ui_element(self.find_element
                                     (ForgotPasswordPageLocators.EMAIL_ADDRESS_INPUT),
                                     email)

    def click_continue_button(self):
        """Click on continue btn method"""
        self.find_element(ForgotPasswordPageLocators.CONTINUE_BUTTON).click()

    def get_alert_text(self):
        """Return text alert or empty string in case no alert is displayed"""
        try:
            element = self.driver.find_element(*ForgotPasswordPageLocators.WARNING_NOT_FOUND_RECORD)

            if element.is_displayed():
                return element.text
            return ''

        except NoSuchElementException:
            print('No such element on the page')
