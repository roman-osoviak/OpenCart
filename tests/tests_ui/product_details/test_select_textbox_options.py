"""Module for testing checkbox selection"""
from pages.product_details_page import ProductDetailsPage
from utils.enums import ProductDetailsPageCheckBox


def test_checkbox_selection(browser, get_env):
    """Testing checkbox options selection"""
    site_url = get_env['environment']['site_url']
    prod_page_details = ProductDetailsPage(browser, site_url)
    prod_page_details.go_to_site()

    prod_page_details.click_on_checkbox(ProductDetailsPageCheckBox.CHECKBOX_OPTION_FIRST, True)
    # to do : verify is selected
