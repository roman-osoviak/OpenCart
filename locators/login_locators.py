"""Module with locators in Login page"""
from selenium.webdriver.common.by import By


# pylint: disable=too-few-public-methods
class LoginPageLocators:
    """Locators for Login page"""
    EMAIL_INPUT = (By.ID, 'input-email')
    PASSWORD_INPUT = (By.ID, 'input-password')
    LOGIN_BUTTON = (By.XPATH, '//*[@type="submit"]')
    CONTINUE_BUTTON = (By.XPATH, '//*[contains(text(), "Continue")]')
