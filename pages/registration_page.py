"""
This module describes Registration Page
RegistrationPage is inherited from BasePage
"""
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
    AGREE_FLAG = (By.NAME, 'agree')
    CONTINUE_BUTTON = (By.XPATH, '//*[@type="submit"]')


class RegitrationPage(BasePage):
    """This class collects methods for Registration Page"""
    _URL_PATH = '?route=account/register'
