"""Module for testing prices"""
from hamcrest import assert_that

from pages.product_details_page import ProductDetailsPage


def test_old_price_is_greater_than_new(browser, get_env):
    """Verify that old price is greater than new one"""
    site_url = get_env['environment']['site_url']
    prod_details_page = ProductDetailsPage(browser, site_url)
    prod_details_page.go_to_site()

    assert_that(prod_details_page.verify_new_price_is_greater_than_old())
