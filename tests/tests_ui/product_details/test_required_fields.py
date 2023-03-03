"""Module for testing requirements field - checking errors in case of null values"""
from pages.product_details_page import ProductDetailsPage


def test_if_required_fields_are_required_indeed(browser, get_env):
    """Testing flow when required fields are not filled"""
    site_url = get_env['environment']['site_url']
    prod_details_page = ProductDetailsPage(browser, site_url)
    prod_details_page.go_to_site()

    prod_details_page \
        .verify_radio_required_error_is_displayed(False) \
        .verify_checkbox_required_error_is_displayed(False) \
        .verify_text_required_error_is_displayed(False) \
        .verify_select_required_error_is_displayed(False) \
        .verify_textarea_required_error_is_displayed(False) \
        .verify_file_required_error_is_displayed(False)

    # preconditions for required error text
    prod_details_page.set_random_string_to_text_input(0)

    prod_details_page \
        .click_on_add_to_cart_button() \
        .verify_radio_required_error_is_displayed() \
        .verify_checkbox_required_error_is_displayed() \
        .verify_text_required_error_is_displayed() \
        .verify_select_required_error_is_displayed() \
        .verify_textarea_required_error_is_displayed() \
        .verify_file_required_error_is_displayed()
