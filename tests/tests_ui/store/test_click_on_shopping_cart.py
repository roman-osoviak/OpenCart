"""Module describes opening hopping cart flow"""

from pages.store_page import StorePage
from utils.constants import PageTitle, StoreItems


def test_click_on_shopping_cart_button(browser, get_env):
    """Opening shopping cart flow"""
    site_url = get_env['environment']['site_url']

    store_page = StorePage(browser, site_url)
    store_page.go_to_site()

    assert browser.title == PageTitle.SHOPPING_CART_PAGE_TITLE
    assert store_page.get_shopping_cart_text() == StoreItems.SHOPPING_CART_BUTTON_ZERO_COST
