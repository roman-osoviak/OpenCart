"""Module to verify Specification tab"""
import allure

from pages.product_details_page import ProductDetailsPage


def test_specification_tab(browser, get_env):
    """Test specification tab"""
    site_url = get_env['environment']['site_url']
    prod_details_page = ProductDetailsPage(browser, site_url)

    with allure.step(f'Opening {site_url}'):
        prod_details_page.go_to_site()
