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
