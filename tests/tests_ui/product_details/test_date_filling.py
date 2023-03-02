"""Module for testing date element"""
from pages.product_details_page import ProductDetailsPage


def test_date_selection(browser, get_env):
    """Positive date selection case"""
    site_url = get_env['environment']['site_url']
    prod_details_page = ProductDetailsPage(browser, site_url)
    prod_details_page.go_to_site()
