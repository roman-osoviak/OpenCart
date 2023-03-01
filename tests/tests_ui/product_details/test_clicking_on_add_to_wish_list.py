"""Module for checking flow with clicking on add to wish list"""
from pages.product_details_page import ProductDetailsPage


def test_click_add_to_wish_list_by_unauthorised_user(browser, get_env):
    """Verifying flow with unauthorized user"""
    site_url = get_env['environment']['site_url']
    prod_details_page = ProductDetailsPage(browser, site_url)
    prod_details_page.go_to_site()

    prod_details_page.verify_alert_is_displayed(False)
    prod_details_page.click_on_add_wish_button()
    prod_details_page.verify_alert_is_displayed()
    # need to check if opacity window shows
    assert 'You must' in prod_details_page.get_alert_text()


def test_click_add_to_wish_list_by_authorised_user(browser, get_env):
    """Verifying flow with authorized user"""
    site_url = get_env['environment']['site_url']
    prod_details_page = ProductDetailsPage(browser, site_url)
    prod_details_page.go_to_site()
