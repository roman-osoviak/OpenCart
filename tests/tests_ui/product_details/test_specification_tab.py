"""Module to verify Specification tab"""
import allure

from pages.product_details_page import ProductDetailsPage
from utils.enums import ProductDetailsTabsLower


def test_specification_tab(browser, get_env):
    """Test specification tab"""
    site_url = get_env['environment']['site_url']
    prod_details_page = ProductDetailsPage(browser, site_url)

    with allure.step(f'Opening {site_url}'):
        prod_details_page.go_to_site()
    with allure.step('Verifying specification tab elements presence'):
        prod_details_page.click_on_tab_lower(ProductDetailsTabsLower.TAB_SPECIFICATION)
        prod_details_page.verify_specification_table_text_is_proper()
