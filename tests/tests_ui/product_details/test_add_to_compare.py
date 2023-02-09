"""Module for testing clicking on 'Compare This Product' button"""
from pages.product_details_page import ProductDetailsPage


def test_click_on_compare_product_button_unauthorised_user(browser, get_env):
    site_url = get_env['environment']['site_url']
    prod_details_page = ProductDetailsPage(browser, site_url)
    prod_details_page.go_to_site()

    prod_details_page.verify_alert_is_displayed(False)
    prod_details_page.click_on_add_compare_button()
    prod_details_page.verify_alert_is_displayed()
    # need to check if opacity window shows
    assert 'Success: You have added' in prod_details_page.get_alert_text()