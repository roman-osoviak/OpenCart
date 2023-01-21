"""
This module describes Registration Page
RegistrationPage is inherited from BasePage
"""
import logging

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


# pylint: disable=too-few-public-methods
class RegistrationLocators:
    """Locators for Registration page"""
    FIRST_NAME_INPUT = (By.XPATH, '//*[@id="input-firstname"]')
    LAST_NAME_INPUT = (By.XPATH, '//*[@id="input-lastname"]')
    EMAIL_INPUT = (By.XPATH, '//*[@id="input-email"]')
    PASSWORD_INPUT = (By.XPATH, '//*[@id="input-password"]')
    SUBSCRIBE_YES = (By.CSS_SELECTOR, '#input-newsletter-yes')
    SUBSCRIBE_NO = (By.CSS_SELECTOR, '#input-newsletter-no')
    SUBSCRIBE_FLAG = (By.NAME, 'agree')
    CONTINUE_BUTTON = (By.XPATH, '//*[@type="submit"]')
    ERRORS_TEXT_ON_PAGE = (By.XPATH, '//*[@class="text-danger"]')


class RegistrationPage(BasePage):
    """This class collects methods for Registration Page"""
    _URL_PATH = '?route=account/register'

    def go_to_site(self):
        """Open registration page method"""
        return self.driver.get(self.base_url + self._URL_PATH)

    # pylint: disable=too-many-arguments
    def register_user(self, first_name: str, last_name: str, email: str,
                      password: str, subscribe_flag: bool):
        """
        User registration procedure

        :param first_name: first Name value
        :param last_name: last Name value
        :param email: email address field value
        :param password: password value
        :param subscribe_flag: subscribe flag value
        :return: None
        """
        logging.info("Trying to register user with %s email and '%s' as a password",
                     email, password)
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_email(email)
        self.set_password(password)
        self.set_subscribe_flag(subscribe_flag)
        self.click_on_continue_btn()
        logging.info("User is successfully registered")

    def set_first_name(self, first_name: str):
        """
        Method to input First Name

        :param first_name: First Name need to be entered
        :return: None
        """
        self.type_text_in_ui_element(
            self.driver.find_element(*RegistrationLocators.FIRST_NAME_INPUT),
            first_name)

    def set_last_name(self, last_name: str):
        """
        Method to input Last Name

        :param last_name: Last Name need to be entered
        :return: None
        """
        self.type_text_in_ui_element(
            self.driver.find_element(*RegistrationLocators.LAST_NAME_INPUT),
            last_name)

    def set_email(self, email: str):
        """
        Input email field

        :param email: Email address need to enter
        :return: None
        """
        self.type_text_in_ui_element(
            self.driver.find_element(*RegistrationLocators.EMAIL_INPUT),
            email)

    def set_password(self, password: str):
        """
        Input password field

        :param password: Password need to enter
        :return: None
        """
        self.type_text_in_ui_element(
            self.driver.find_element(*RegistrationLocators.PASSWORD_INPUT),
            password)

    def set_subscribe_flag(self, subscribe_state: bool):
        """
        Method to set yes or no for subscription

        :param subscribe_state: Check subscribe flag is True, otherwise False
        :return: state of check-box
        """
        return self._trigger_checkbox(RegistrationLocators.SUBSCRIBE_FLAG, subscribe_state)

    def click_on_continue_btn(self):
        """
        Press Continue button method

        :return: None
        """
        return self.find_element(RegistrationLocators.CONTINUE_BUTTON).click()

    def get_errors_count(self):
        """
        Count a number of error text on the page

        :return: Number of errors on the page
        """

        error_counter = 0
        for element in self.find_elements(RegistrationLocators.ERRORS_TEXT_ON_PAGE):
            error_counter += 1
            print(element)
        return error_counter

    def get_error_message(self, error_text: RegPageErrorType):
        """
        Return specific error text

        :param error_text: specific id field where error occurs
        :return: error text
        """

        return self.find_element((By.XPATH,
                                  (RegistrationLocators.ERROR_XPATH.format(error_text.value)))).text
