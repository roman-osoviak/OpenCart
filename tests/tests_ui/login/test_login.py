"""
Module with test case for testing login is successful
"""

from pages.login_page import LoginPage
from utils.constants import PageTitle


def test_login(browser, get_env):
    """Basic login success flow"""
    site_url = get_env['environment']['site_url']
    email = get_env['user']['existing_email']
    password = get_env['user']['password']

    class_page = LoginPage(browser, site_url)
    class_page.go_to_site()

    assert browser.title == PageTitle.LOGIN_PAGE_TITLE

    class_page.login(email, password)

    # after success login user should see specific title
    assert browser.title == PageTitle.MY_ACCOUNT_PAGE_TITLE
