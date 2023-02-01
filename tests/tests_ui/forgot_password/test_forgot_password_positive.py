"""
Module with test case for testing forgot password positive flow
"""

from pages.forgot_password_page import ForgotPasswordPage
from utils.common import get_random_email
from utils.constants import PageTitle


def test_forgot_password(browser, get_env):
    """Positive forgot password flow"""
    site_url = get_env['environment']['site_url']

    class_page = ForgotPasswordPage(browser, site_url)
    class_page.go_to_site()

    assert browser.title == PageTitle.FORGOT_PASSWORD_PAGE_TITLE

    class_page.forgot_password(get_random_email())
    assert browser.title == PageTitle.FORGOT_PASSWORD_SUCCESS
