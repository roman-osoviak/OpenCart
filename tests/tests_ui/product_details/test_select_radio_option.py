"""Module for testing radio options"""

from pages.product_details_page import ProductDetailsPage, ProductDetailsLocators
from utils.enums import ProductDetailsPageRadio


def test_radio_option_selection(browser, get_env):
    """Select option"""
    site_url = get_env['environment']['site_url']
    prod_details_page = ProductDetailsPage(browser, site_url)
    prod_details_page.go_to_site()

    # first radio option
    assert not prod_details_page.verify_radio_button_is_selected(
        ProductDetailsLocators.RADIO_BUTTON_FIRST)
    prod_details_page.click_on_radio_button(ProductDetailsPageRadio.RADIO_OPTION_FIRST)
    assert prod_details_page.verify_radio_button_is_selected(
        ProductDetailsLocators.RADIO_BUTTON_FIRST)

    # second radio option
    assert not prod_details_page.verify_radio_button_is_selected(
        ProductDetailsLocators.RADIO_BUTTON_SECOND)
    prod_details_page.click_on_radio_button(ProductDetailsPageRadio.RADIO_OPTION_SECOND)
    assert prod_details_page.verify_radio_button_is_selected(
        ProductDetailsLocators.RADIO_BUTTON_SECOND)

    # third radio option
    assert not prod_details_page.verify_radio_button_is_selected(
        ProductDetailsLocators.RADIO_BUTTON_THIRD)
    prod_details_page.click_on_radio_button(ProductDetailsPageRadio.RADIO_OPTION_THIRD)
    assert prod_details_page.verify_radio_button_is_selected(
        ProductDetailsLocators.RADIO_BUTTON_THIRD)
