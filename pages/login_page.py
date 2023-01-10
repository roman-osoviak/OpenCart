"""
This module describes Login Page
LoginPage is inherited from BasePage
"""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


# pylint: disable=too-few-public-methods
class LoginPageLocators:
    """Locators for Login page"""
    EMAIL_INPUT = (By.ID, 'input-email')
    PASSWORD_INPUT = (By.ID, 'input-password')
    LOGIN_BUTTON = (By.XPATH, '//*[@type="submit"]')


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
       :return:
       """
        self.set_email(email)
        self.set_password(password)
        self.click_login_btn()
        print("pass")

    def set_email(self, email: str):
        """
        Input email field

        :param email: email address need to enter
        :return:
        """
        self.type_text_in_ui_element(self.driver.find_element(*LoginPageLocators.EMAIL_INPUT),
                                     email)

    def set_password(self, password: str):
        """
        Input password field

        :param password: password field need to enter
        :return:
        """
        self.type_text_in_ui_element(self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT),
                                     password)

    def click_login_btn(self):
        """Click on Login btn"""
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()
