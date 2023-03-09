"""Module for testing prices"""
from hamcrest import assert_that

from pages.product_details_page import ProductDetailsPage
from utils.enums import ColorsInHexString


def test_old_price_is_greater_than_new(browser, get_env):
    """Verify that old price is greater than new one"""
    site_url = get_env['environment']['site_url']
    prod_details_page = ProductDetailsPage(browser, site_url)
    prod_details_page.go_to_site()

    assert_that(prod_details_page.verify_old_price_is_greater_than_new())
    assert prod_details_page.get_old_price_color() == ColorsInHexString.OLD_PRICE.value
