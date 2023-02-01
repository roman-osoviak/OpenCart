"""Module to check an ability to click & navigate to registration page"""

from pages.login_page import LoginPage
from utils.constants import PageTitle


def test_ability_to_open_registration(browser, get_env):
    """Check state transition from Login to Register page"""
    site_url = get_env['environment']['site_url']

    class_page = LoginPage(browser, site_url)
    class_page.go_to_site()
    assert browser.title == PageTitle.LOGIN_PAGE_TITLE
    class_page.click_continue_button()

    # User should be on Registration Page
    assert browser.title == PageTitle.REGISTRATION_PAGE_TITLE
