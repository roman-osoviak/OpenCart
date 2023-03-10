"""Module for testing radio text labels"""
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

    # small option checking
    prod_details_page \
        .click_on_radio_button(ProductDetailsPageRadio.RADIO_OPTION_FIRST) \
        .verify_radio_button_label(ProductDetailsPageRadio.RADIO_OPTION_FIRST,
                                   'Small (+$14.00)')
    # medium option checking
    prod_details_page \
        .click_on_radio_button(ProductDetailsPageRadio.RADIO_OPTION_SECOND) \
        .verify_radio_button_label(ProductDetailsPageRadio.RADIO_OPTION_SECOND,
                                   'Medium (+$26.00)')
    # large option checking
    prod_details_page \
        .click_on_radio_button(ProductDetailsPageRadio.RADIO_OPTION_THIRD) \
        .verify_radio_button_label(ProductDetailsPageRadio.RADIO_OPTION_THIRD,
                                   'Large (+$38.00)')
