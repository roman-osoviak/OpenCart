"""Module with locators on Forgot Password page"""
from selenium.webdriver.common.by import By


# pylint: disable=too-few-public-methods
class ForgotPasswordPageLocators:
    """Locators for Forgotten Password page"""
    EMAIL_ADDRESS_INPUT = (By.XPATH, '//*[@name="email"]')
    BACK_BUTTON = (By.XPATH, '//*[contains(text(), "Back")]')
    CONTINUE_BUTTON = (By.XPATH, '//*[@type="submit"]')
    WARNING_NOT_FOUND_RECORD = (By.XPATH, '//*[@id="alert"]/div')
