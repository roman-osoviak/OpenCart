"""Verifying select drop-down menu"""

from pages.product_details_page import ProductDetailsPage
from utils.enums import ProductDetailsPageSelectMenu


def test_select_drop_down_menu(browser, get_env):
    """Test drop-down"""
    site_url = get_env['environment']['site_url']
    prod_details_page = ProductDetailsPage(browser, site_url)
    prod_details_page.go_to_site()

    # verify default selection
    assert prod_details_page.get_selected_option_text_from_select() == \
           ProductDetailsPageSelectMenu.VALUE_ZERO.value.strip()
    prod_details_page.select_option_by_value('1')
    prod_details_page.select_option_by_value('2')
    prod_details_page.select_option_by_value('3')
    prod_details_page.select_option_by_value('4')
