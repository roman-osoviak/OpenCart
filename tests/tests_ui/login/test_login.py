"""
Module with test case for testing login is successful
"""

from selenium import webdriver
from pages.login_page import LoginPage
from utils.constants import PageTitle


def test_login(browser, get_env):
    """Basic login success flow"""
    site_url = get_env['environment']['site_url']
    class_page = LoginPage(browser, site_url)
    class_page.go_to_site()

    assert browser.title == PageTitle.LOGIN_PAGE_TITLE
