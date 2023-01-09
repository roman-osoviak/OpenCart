"""
This module describes Login Page
LoginPage is inherited from BasePage
"""

from pages.base_page import BasePage


class LoginPage(BasePage):
    """This class collects methods for Base Page"""
    _URL_PATH = '?route=account/login'

    def go_to_site(self):
        """Open login page"""
        return self.driver.get(self.base_url + self._URL_PATH)

    def login(self, email: str, password: str):
        """
       Positive login procedure

       :param email: email address to login with
       :param password:  password to login with
       :return:
       """
        self.set_email(email)
        self.set_password(password)
        self.click_login_btn()

    def set_email(self, email: str):
        """
        Input email field

        :param email: email address need to enter
        :return:
        """

    def set_password(self, password: str):
        """
        Input password field

        :param password: password field need to enter
        :return:
        """

    def click_login_btn(self):
        """Click on Login btn"""
