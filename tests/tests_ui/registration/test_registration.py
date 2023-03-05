"""
This module consists of test cases for checking basic registration success flow
on the Registration Page
"""
from pages.registration_page import RegistrationPage
from utils.common import get_random_string, fake
from utils.constants import PageTitle


def test_user_registration(browser, get_env):
    """User registration"""

    site_url = get_env['environment']['site_url']
    password = get_random_string(4)

    class_page = RegistrationPage(browser, site_url)
    class_page.go_to_site()

    assert browser.title == PageTitle.REGISTRATION_PAGE_TITLE

    email_address = fake.email()
    class_page.register_user(fake.first_name(), fake.last_name(),
                             email_address, password, True)
    # after success registration user should see specific title
    assert browser.title == PageTitle.REGISTERED_PAGE_TITLE
