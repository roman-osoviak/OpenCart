"""For managing driver"""

from selenium import webdriver
from utils.enums import BrowserDefinition


def get_driver(browser: BrowserDefinition):
    """
    Manage browser

    :param browser: specify browser name to run tests with
    :return: specific browser's driver
    """
    if browser == BrowserDefinition.CHROME:
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless")
    if browser == BrowserDefinition.FIREFOX:
        return webdriver.Firefox(executable_path="geckodriver")
    return webdriver.Chrome(executable_path="chromedriver", chrome_options=options)
