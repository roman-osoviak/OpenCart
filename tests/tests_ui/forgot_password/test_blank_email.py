"""
Module with test case for testing forgot password positive flow
"""

from pages.forgot_password_page import ForgotPasswordPage
from utils.constants import PageTitle
from utils.constants import ForgotPasswordPageWarning


def test_empty_email(browser, get_env):
    """Negative scenario with an empty email"""
    site_url = get_env['environment']['site_url']
    class_page = ForgotPasswordPage(browser, site_url)
    class_page.go_to_site()

    class_page.forgot_password()
    assert class_page.get_alert_text() == ForgotPasswordPageWarning.EMAIL_NOT_FOUND
    assert browser.title == PageTitle.FORGOT_PASSWORD_PAGE_TITLE
