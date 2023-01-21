"""
This module consists of test cases for checking last_name input
on the Registration Page
"""

import pytest

from pages.registration_page import RegistrationPage
from utils.common import get_random_first_name, get_random_email, \
    get_random_string
from utils.constants import RegPageError
from utils.enums import RegPageErrorType

test_data = ['', ' ', get_random_string(33)]


@pytest.mark.parametrize('test_input', test_data)
def test_invalid_last_name(browser, test_input, get_env):
    """
    Check last_name required field error
    Check error message because of SPACE is not valid last_name
    Check error text in case invalid last_name length
    """
    password = get_random_string(5)
    site_url = get_env['environment']['site_url']

    class_page = RegistrationPage(browser, site_url)
    class_page.go_to_site()
    class_page.register_user(get_random_first_name(), test_input, get_random_email(),
                             password, True)

    assert class_page.get_errors_count() == 1
    assert class_page.get_error_message(RegPageErrorType.LAST_NAME) == RegPageError.BAD_LAST_NAME
