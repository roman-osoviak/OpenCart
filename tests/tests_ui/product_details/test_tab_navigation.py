"""Module for testing low tabs navigation"""
from pages.product_details_page import ProductDetailsPage
from utils.enums import ProductDetailsTabsLower


def test_tab_navigation(browser, get_env):
    """Verifying that navigation through tabs works as expected"""
    site_url = get_env['environment']['site_url']
    prod_details_page = ProductDetailsPage(browser, site_url)
    prod_details_page.go_to_site()

    prod_details_page.click_on_tab_lower(ProductDetailsTabsLower.TAB_SPECIFICATION)
    prod_details_page.verify_tab_is_active(ProductDetailsTabsLower.TAB_SPECIFICATION)
