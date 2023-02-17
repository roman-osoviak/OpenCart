"""Module for testing radio text label"""
from pages.product_details_page import ProductDetailsPage
from utils.enums import ProductDetailsPageRadio


def test_text_from_selected_radio(browser, get_env):
    """
    Verifying text from currently selected radio option


    :return: None
    """
    site_url = get_env['environment']['site_url']
    prod_details_page = ProductDetailsPage(browser, site_url)
    prod_details_page.go_to_site()

    prod_details_page.click_on_radio_button(ProductDetailsPageRadio.RADIO_OPTION_FIRST)
    prod_details_page.get_text_attribute_value(ProductDetailsPageRadio.RADIO_OPTION_FIRST)
