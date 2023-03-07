"""
This module describes Login Page
LoginPage is inherited from BasePage
"""
import logging

from locators.login_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    """This class collects methods for Base Page"""
    _URL_PATH = '?route=account/login'

    def go_to_site(self):
        """Open login page"""
        return self.driver.get(self.base_url + self._URL_PATH)

    def login(self, email: str, password: str):
        """
       Login method implementation

       :param email: email address to login with
       :param password:  password to login with
       :return: None
       """
        logging.info("Trying to register user with %s email and '%s' as a password",
                     email, password)
        self.set_email(email)
        self.set_password(password)
        self.click_login_button()
        logging.info("Login is successful")

    def set_email(self, email: str):
        """
        Input email field

        :param email: email address need to enter
        :return: None
        """
        self.type_text_in_ui_element(self.driver.find_element(*LoginPageLocators.EMAIL_INPUT),
                                     email)

    def set_password(self, password: str):
        """
        Input password field

        :param password: password field need to enter
        :return: None
        """
        self.type_text_in_ui_element(self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT),
                                     password)

    def click_login_button(self):
        """Click on Login button"""
        self.click_on_element(LoginPageLocators.LOGIN_BUTTON)

    def click_continue_button(self):
        """Click on Continue button"""
        self.click_on_element(LoginPageLocators.CONTINUE_BUTTON)
