"""Module with locators in Registration Page"""
from selenium.webdriver.common.by import By


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
    ERROR_XPATH = '//input[@id="{}"]/following-sibling::*'
