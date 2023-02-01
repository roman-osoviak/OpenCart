"""Common Test Configuration Module"""
import logging
import os
import os.path

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
