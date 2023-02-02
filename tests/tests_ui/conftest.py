"""Configuration module for UI tests only"""
import os.path
from datetime import datetime

import allure
import pytest
from allure_commons.types import AttachmentType

from utils.driver_manager import BrowserDefinition, get_driver


@pytest.fixture(scope="function")
def browser():
    """Browser's fixture"""
    driver = get_driver(BrowserDefinition.CHROME)

    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Test reports/failures and screenshots in case of failed tests"""
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    # we only look at actual failing test calls, not setup/teardown
    if rep.when == "call" and rep.failed:
        now = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        base_path = os.path.dirname(__file__)

        screen_file_path = os.path.abspath("{}/{}_{}.png".format(base_path, item.name, str(now)))

        if 'browser' in item.fixturenames:
            item.funcargs['browser'].save_screenshot(screen_file_path)
        else:
            print('Fail to take screen-shot')

        attach_title_name = '{}_{}'.format(item.name, str(now))
        allure.attach.file(screen_file_path, attach_title_name, attachment_type=AttachmentType.PNG)

        # if you don't want to see screenshots in your folder just comment next lines
        # for file in os.listdir(base_path):
        #     if file.endswith('.png'):
        #         os.remove(os.path.join(base_path + '/', file))
