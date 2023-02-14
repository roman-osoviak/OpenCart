"""Module for testing radio options"""
from hamcrest import assert_that

from pages.product_details_page import ProductDetailsPage
from utils.enums import ProductDetailsPageRadio


def test_radio_option_selection(browser, get_env):
    """Select option"""
    site_url = get_env['environment']['site_url']
    prod_details_page = ProductDetailsPage(browser, site_url)
    prod_details_page.go_to_site()

    assert_that(prod_details_page.get_radio_label_text(1) ==
                ProductDetailsPageRadio.RADIO_OPTION_FIRST.value)
    assert_that(prod_details_page.get_radio_label_text(2) ==
                ProductDetailsPageRadio.RADIO_OPTION_SECOND.value)
    assert_that(prod_details_page.get_radio_label_text(3) ==
                ProductDetailsPageRadio.RADIO_OPTION_THIRD.value)
