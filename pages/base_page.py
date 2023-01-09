"""
This module describes top level Base Page
"""


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
