"""Module for testing textarea input"""
from pages.product_details_page import ProductDetailsPage


def test_input_text_to_textarea(browser, get_env):
    """Test method for checking input text to textarea"""
    site_url = get_env['environment']['site_url']
    prod_page_details = ProductDetailsPage(browser, site_url)
    prod_page_details.go_to_site()

    # check default text and placeholder at once
