"""Test Module for verifying that default currency is USD"""
from pages.store_page import StorePage


def test_default_currency_is_usd(browser, get_env):
    """Checks that USD is default selected"""
    site_url = get_env['environment']['site_url']
    store_page = StorePage(browser, site_url)
    store_page.go_to_site()
    assert store_page.verify_selected_currency_dropdown()
