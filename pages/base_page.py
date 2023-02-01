"""
This module describes top level Base Page
"""

from typing import Tuple

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """This class collects methods for Base Page"""

    def __init__(self, driver, base_url: str):
        self.driver = driver
        self.base_url = base_url

    def go_to_site(self):
        """
        Open default page

        :return: get page
        """
        return self.driver.get(self.base_url)

    def find_element(self, locator: Tuple):
        """
        Find specific element by locator

        :param locator: locator itself
        :return: webElement from HTML tree
        """
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator: Tuple, time=10):
        """
        Wrapper for webdriver find_elements method

        :param locator: locator itself
        :param time: time to wait for an element
        :return: webElements from HTML tree
        """
        return WebDriverWait(self.driver, time). \
            until(EC.presence_of_all_elements_located(locator),
                  message=f"Can't find elements by locator {locator}")

    @staticmethod
    def type_text_in_ui_element(locator: Tuple, text: str):
        """
        Method for typing into inputs.
        UI element will be cleared before actual input.

        :param locator: locator itself
        :param text: string to input
        :return:
        """
        elem = locator
        elem.clear()
        elem.send_keys(text)

    def _trigger_checkbox(self, locator: Tuple, value: bool):
        """
        Selecting/deselecting checkbox according to the provided value

        :param locator: locator that describes an element
        :param value: True in case we need to check, otherwise False
        :return: None
        """
        state = self.find_element(locator).is_selected()
        if value != state:
            self.find_element(locator).click()

    def click_on_element(self, locator: Tuple):
        """
        Click on UI element

        :param locator: locator itself
        :return: None
        """
        self.find_element(locator).click()

    def get_element_text(self, locator: Tuple):
        """
        Get text from element

        :param locator: locator itself
        :return: element text
        """
        return self.find_element(locator).text
