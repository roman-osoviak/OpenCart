"""Module for testing checkbox selection"""

from pages.product_details_page import ProductDetailsPage
from utils.enums import ProductDetailsPageCheckBox


def test_checkbox_selection(browser, get_env):
    """Testing checkbox options selection"""
    site_url = get_env['environment']['site_url']
    prod_page_details = ProductDetailsPage(browser, site_url)
    prod_page_details.go_to_site()

    # options should be not selected by default
    prod_page_details \
        .verify_checkbox_is_selected(ProductDetailsPageCheckBox.CHECKBOX_OPTION_FIRST, False) \
        .click_on_checkbox(ProductDetailsPageCheckBox.CHECKBOX_OPTION_FIRST, True) \
        .verify_checkbox_is_selected(ProductDetailsPageCheckBox.CHECKBOX_OPTION_FIRST, True)

    prod_page_details \
        .verify_checkbox_is_selected(ProductDetailsPageCheckBox.CHECKBOX_OPTION_SECOND, False) \
        .click_on_checkbox(ProductDetailsPageCheckBox.CHECKBOX_OPTION_SECOND, True) \
        .verify_checkbox_is_selected(ProductDetailsPageCheckBox.CHECKBOX_OPTION_SECOND, True)

    prod_page_details \
        .verify_checkbox_is_selected(ProductDetailsPageCheckBox.CHECKBOX_OPTION_THIRD, False) \
        .click_on_checkbox(ProductDetailsPageCheckBox.CHECKBOX_OPTION_THIRD, True) \
        .verify_checkbox_is_selected(ProductDetailsPageCheckBox.CHECKBOX_OPTION_THIRD, True)

    prod_page_details \
        .verify_checkbox_is_selected(ProductDetailsPageCheckBox.CHECKBOX_OPTION_FOURTH, False) \
        .click_on_checkbox(ProductDetailsPageCheckBox.CHECKBOX_OPTION_FOURTH, True) \
        .verify_checkbox_is_selected(ProductDetailsPageCheckBox.CHECKBOX_OPTION_FOURTH, True)
