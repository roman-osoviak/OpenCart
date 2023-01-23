"""Module describes opening hopping cart flow"""

from pages.store_page import StorePage
from utils.constants import PageTitle


def test_click_on_shopping_cart_button(browser, get_env):
    """Opening shopping cart flow"""
    site_url = get_env['environment']['site_url']

    class_page = StorePage(browser, site_url)
    class_page.go_to_site()

    assert browser.title == PageTitle.SHOPPING_CART_PAGE_TITLE

    # class_page.click_on_shopping_cart()
    assert class_page.empty_shopping_cart_menu_displayed()
