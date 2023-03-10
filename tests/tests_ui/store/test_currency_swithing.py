"""Module for validating proper currency switching"""
from pages.store_page import StorePage
from utils.enums import Currency, StoreCurrency


def test_currency_switching(browser, get_env):
    """Testing proper text for specific currency"""

    site_url = get_env['environment']['site_url']

    store_page = StorePage(browser, site_url)
    store_page.go_to_site()

    # select EURO and check certain text
    store_page.select_currency(Currency.EURO)
    # on shopping cart button
    store_page.verify_shopping_cart_button_text(StoreCurrency.SHOPPING_CART_BUTTON_ZERO_COST_EURO)
    # and for currency drop-down sign
    store_page.verify_selected_currency_dropdown(Currency.EURO)

    # select POUNDS and check certain text
    store_page.select_currency(Currency.POUNDS)
    store_page.verify_shopping_cart_button_text(StoreCurrency.SHOPPING_CART_BUTTON_ZERO_COST_POUND)
    store_page.verify_selected_currency_dropdown(Currency.POUNDS)

    # select USD and check certain text
    store_page.select_currency(Currency.USD)
    store_page.verify_shopping_cart_button_text(StoreCurrency.SHOPPING_CART_BUTTON_ZERO_COST_USD)
    # we need to check if sign before currency dropdown is also changed
    store_page.verify_selected_currency_dropdown(Currency.USD)
