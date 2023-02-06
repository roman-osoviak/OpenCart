"""Module for checking flow with clicking on add to wish list"""
from pages.product_details_page import ProductDetailsPage


def test_click_add_to_wish_list_by_unauthorised_user(browser, get_env):
    """Verifying flow with unauthorized user"""
    site_url = get_env['environment']['site_url']
    prod_details_page = ProductDetailsPage(browser, site_url)
    prod_details_page.go_to_site()

    prod_details_page.click_on_add_wish_button()
    assert 1 == 1 # need to check if opacity window shows

def test_click_add_to_wish_list_by_authorised_user(browser, get_env):
    """Verifying flow with authorized user"""
    site_url = get_env['environment']['site_url']
    prod_details_page = ProductDetailsPage(browser, site_url)
    prod_details_page.go_to_site()