"""
This module consists of test cases for checking first_name input
on the Registration Page
"""

import pytest

from pages.registration_page import RegistrationPage
from utils.common import get_random_string, get_random_last_name, get_random_email
from utils.enums import RegPageErrorType

test_data = ['', ' ', get_random_string(33, 'lower')]


@pytest.mark.parametrize('test_input', test_data)
def test_invalid_first_name(browser, get_env, test_input):
    """Testing invalid inputs for first_name field"""

    password = get_random_string(5)
    site_url = get_env['environment']['site_url']

    class_page = RegistrationPage(browser, site_url)
    class_page.go_to_site()
    class_page.register_user(test_input, get_random_last_name(), get_random_email(), password, True)

    assert class_page.get_errors_count() == 1
    assert class_page.get_error_message(RegPageErrorType.FIRST_NAME)
