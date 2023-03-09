"""Module for testing low tabs navigation"""
import allure

from pages.product_details_page import ProductDetailsPage
from utils.enums import ProductDetailsTabsLower


def test_tab_navigation(browser, get_env):
    """Verifying that navigation through tabs works as expected"""
    site_url = get_env['environment']['site_url']
    prod_details_page = ProductDetailsPage(browser, site_url)

    with allure.step(f'Opening {site_url}'):
        prod_details_page.go_to_site()

    # check navigation through the tabs
    with allure.step('Checking tabs navigation'):
        prod_details_page \
            .verify_tab_is_active(ProductDetailsTabsLower.TAB_DESCRIPTION) \
            .click_on_tab_lower(ProductDetailsTabsLower.TAB_SPECIFICATION) \
            .verify_tab_is_active(ProductDetailsTabsLower.TAB_SPECIFICATION) \
            .click_on_tab_lower(ProductDetailsTabsLower.TAB_REVIEWS) \
            .verify_tab_is_active(ProductDetailsTabsLower.TAB_REVIEWS) \
            .click_on_tab_lower(ProductDetailsTabsLower.TAB_DESCRIPTION) \
            .verify_tab_is_active(ProductDetailsTabsLower.TAB_DESCRIPTION)
