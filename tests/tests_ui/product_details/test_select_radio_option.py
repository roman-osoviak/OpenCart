"""Module for testing radio options"""
from pages.product_details_page import ProductDetailsPage


def test_radio_option_selection(browser, get_env):
    """Select option"""
    site_url = get_env['environment']['site_url']
    prod_details_page = ProductDetailsPage(browser, site_url)
    prod_details_page.go_to_site()

    prod_details_page.click_on_radio_option()
