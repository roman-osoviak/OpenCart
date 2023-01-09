"""Common Test Configuration Module"""
import pytest
import os
import yaml


@pytest.fixture(scope="session")
def get_env(request):
    """
     Get environment fixture
     Reading config yml file
     """
    project_path = os.path.dirname(os.path.dirname(__file__))
    with open("{}/config.yml".format(project_path), "r") as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
    return cfg
