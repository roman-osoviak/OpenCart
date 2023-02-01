"""Module for validating proper currency switching"""
from pages.store_page import StorePage
from utils.enums import Currency, StoreCurrency


def test_currency_switching(browser, get_env):
    """Testing proper text for specific currency"""

    site_url = get_env['environment']['site_url']

    store_page = StorePage(browser, site_url)
    store_page.go_to_site()

    store_page.select_currency(Currency.POUNDS)
    assert StoreCurrency.SHOPPING_CART_BUTTON_ZERO_COST_EURO

