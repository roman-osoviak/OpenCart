"""Common Test Configuration Module"""
import logging
import os
import os.path
import pathlib
from datetime import datetime

import allure
import pytest
import yaml


@pytest.fixture(scope="session")
def get_env(request):
    """
     Get environment fixture
     Reading config yml file
     """
    project_path = os.path.dirname(os.path.dirname(__file__))
    # with open("{}/config.yml".format(project_path), "r") as ymlfile:
    with open(f"{project_path}/config.yml", "r") as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
    return cfg


def pytest_configure(config):
    """Logging settings is settings before all"""
    project_path = os.path.dirname(os.path.dirname(__file__))
    log_format = "%(levelname)s %(asctime)s - %(message)s"
    logging.basicConfig(
        # filename='{}/my_log.log'.format(project_path),
        filename=f'{project_path}/my_log.log',
        level=logging.INFO, format=log_format, filemode='w')

    # allure report setup
    allure_folder = pathlib.Path(__file__).parent / "allure_result_folder"
    config.option.allure_report_dir = allure_folder


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item) -> None:
    """
    When the test fails, take a screenshot automatically and display
    it in the allure report.

    :param item: Builtin fixture
    :return: None
    """

    outcome = yield
    report = outcome.get_result()

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            allure_folder = pathlib.Path(__file__).parent / "allure_result_folder"
            now_time = datetime.now().strftime("%Y%m%d%H%M%S")
            screen_path = os.path.join(allure_folder, "{}.png".format(now_time))
            feature_request = item.funcargs['request']
            driver = feature_request.getfixturevalue("browser")
            driver.save_screenshot(screen_path)
            allure.attach.file(screen_path, now_time, allure.attachment_type.PNG)
