"""Configuration module for UI tests only"""

import pytest

from utils.driver_manager import BrowserDefinition, get_driver


@pytest.fixture(scope="function")
def browser():
    """Browser's fixture"""
    driver = get_driver(BrowserDefinition.CHROME)

    yield driver
    driver.quit()
