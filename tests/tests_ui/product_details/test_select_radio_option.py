"""Module for testing radio options"""

from pages.product_details_page import ProductDetailsPage
from utils.enums import ProductDetailsPageRadio


def test_radio_option_selection(browser, get_env):
    """Select option"""
    site_url = get_env['environment']['site_url']
    prod_details_page = ProductDetailsPage(browser, site_url)
    prod_details_page.go_to_site()

    # first radio option
    prod_details_page \
        .verify_radio_button_is_selected(ProductDetailsPageRadio.RADIO_OPTION_FIRST, False) \
        .click_on_radio_button(ProductDetailsPageRadio.RADIO_OPTION_FIRST) \
        .verify_radio_button_is_selected(ProductDetailsPageRadio.RADIO_OPTION_FIRST)

    # second radio option
    prod_details_page \
        .verify_radio_button_is_selected(ProductDetailsPageRadio.RADIO_OPTION_SECOND, False) \
        .click_on_radio_button(ProductDetailsPageRadio.RADIO_OPTION_SECOND) \
        .verify_radio_button_is_selected(ProductDetailsPageRadio.RADIO_OPTION_SECOND)

    # third radio option
    prod_details_page \
        .verify_radio_button_is_selected(ProductDetailsPageRadio.RADIO_OPTION_THIRD, False) \
        .click_on_radio_button(ProductDetailsPageRadio.RADIO_OPTION_THIRD) \
        .verify_radio_button_is_selected(ProductDetailsPageRadio.RADIO_OPTION_THIRD)
