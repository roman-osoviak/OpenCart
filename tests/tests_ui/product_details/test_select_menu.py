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

    prod_details_page.select_option_by_attribute_value('1')
    assert prod_details_page.get_selected_option_text_from_select() == \
           'Green (+$3.20)'

    prod_details_page.select_option_by_attribute_value('2')
    assert prod_details_page.get_selected_option_text_from_select() == \
           'Yellow (+$4.40)'

    prod_details_page.select_option_by_attribute_value('3')
    assert prod_details_page.get_selected_option_text_from_select() == \
           'Blue (+$5.60)'

    prod_details_page.select_option_by_attribute_value('4')
    assert prod_details_page.get_selected_option_text_from_select() == \
           'Red (+$6.80)'
