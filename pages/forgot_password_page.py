"""
This module describes Login Page
LoginPage is inherited from BasePage
"""
from selenium.common import NoSuchElementException

from locators.forgot_password_locators import ForgotPasswordPageLocators
from pages.base_page import BasePage


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
        self.type_text_in_ui_element(ForgotPasswordPageLocators.EMAIL_ADDRESS_INPUT,
                                     email)

    def click_continue_button(self):
        """Click on continue btn method"""
        self.find_element(ForgotPasswordPageLocators.CONTINUE_BUTTON).click()

    def get_alert_text(self):
        """Return text alert or empty string in case no alert is displayed"""
        element_text = ''
        try:
            element = self.driver.find_element(*ForgotPasswordPageLocators.WARNING_NOT_FOUND_RECORD)

            if element.is_displayed():
                element_text = element.text

        except NoSuchElementException:
            print('No such element on the page')

        return element_text
