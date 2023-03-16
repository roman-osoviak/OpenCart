"""Module for testing clicking on 'Compare This Product' button"""
import allure

from pages.product_details_page import ProductDetailsPage


def test_click_on_compare_product_button_unauthorised_user(browser, get_env):
    """Test flow with adding item to the compare list as unauthorised user"""
    site_url = get_env['environment']['site_url']
    prod_details_page = ProductDetailsPage(browser, site_url)
    with allure.step(f'Opening {site_url}'):
        prod_details_page.go_to_site()
    with allure.step('Testing if alert window is shown'):
        prod_details_page \
            .verify_alert_is_displayed(False) \
            .click_on_add_compare_button() \
            .verify_alert_is_displayed()
    # need to check if opacity window shows
    assert 'Success: You have added' in prod_details_page.get_alert_text()
