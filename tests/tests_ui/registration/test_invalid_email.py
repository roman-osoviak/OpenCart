"""
This module consists of test cases for checking email input
on the Registration Page
"""

from pages.registration_page import RegistrationPage
from utils.common import get_random_string, fake
from utils.constants import RegPageError
from utils.enums import RegPageErrorType


def test_blank_email(browser, get_env):
    """Check email required field error"""
    password = get_random_string(5)
    site_url = get_env['environment']['site_url']

    class_page = RegistrationPage(browser, site_url)
    class_page.go_to_site()
    class_page.register_user(fake.first_name(), fake.last_name(),
                             '', password, True)

    assert class_page.get_errors_count() == 1
    assert class_page.get_error_message(RegPageErrorType.EMAIL) == RegPageError.BAD_EMAIL
