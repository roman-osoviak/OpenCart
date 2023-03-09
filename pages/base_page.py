"""
This module describes top level Base Page
"""

from typing import Tuple

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.common import retry


class BasePage:
    """This class collects methods for Base Page"""

    def __init__(self, driver, base_url: str):
        """Constructor"""
        self.driver = driver
        self.base_url = base_url
        self.driver.maximize_window()

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

    def type_text_in_ui_element(self, locator: Tuple, text: str):
        """
        Method for typing into inputs.
        UI element will be cleared before actual input.

        :param locator: locator itself
        :param text: string to input
        :return: self
        """
        elem = self.find_element(locator)
        elem.clear()
        elem.send_keys(text)
        return self

    @retry(20)
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

    @retry(10)
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

    def is_element_displayed(self, locator: Tuple):
        """
        Method that checks if element is displayed with EC (10 sec pause)

        :param locator: locator itself
        :return: True if element displayed, otherwise False
        """
        try:
            self.find_element(locator)
            return True
        except TimeoutException:
            return False

    def is_element_selected(self, locator: Tuple):
        """
        Method checks if element is selected

        :param locator: locator itself
        :return: True if selected, False otherwise
        """
        assert self.find_element(locator).is_selected()

    def is_element_not_selected(self, locator: Tuple):
        """
        Method checks if element is not selected

        :param locator: locator itself
        :return: True if not selected, False otherwise
        """
        assert not self.find_element(locator).is_selected()

    def is_element_invisible(self, locator: Tuple):
        """
        Method that checks if element is displayed without 10 sec pause

        :param locator: locator itself
        :return: True if element displayed, otherwise False
        """
        try:
            self.driver.find_element(By.XPATH, locator[1])
            return False
        except NoSuchElementException:
            return True

    def get_element_attribute(self, locator: Tuple, attribute: str):
        """
        Method that returns attribute by provided locator

        :param locator: locator itself
        :param attribute: locator attribute
        :return: value of the attribute
        """
        return self.find_element(locator).get_attribute(attribute)

    def get_value_of_css_property(self, locator: Tuple, css_property: str):
        """
        Method that returns css property value

        :param locator: locator itself
        :param css_property: desired property name
        :return: str - value of property
        """
        return self.find_element(locator).value_of_css_property(css_property)
