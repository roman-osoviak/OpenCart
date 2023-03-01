"""This module tests that already non-default option can be deselected to default one"""
import random

from pages.product_details_page import ProductDetailsPage
from utils.enums import ProductDetailsPageSelectMenu


def test_selected_option_can_be_changed_to_default(browser, get_env):
    """Verifying that non-default selected option can be changed to default"""
    site_url = get_env['environment']['site_url']
    prod_details_page = ProductDetailsPage(browser, site_url)
    prod_details_page.go_to_site()

    assert prod_details_page.get_selected_option_text_from_select() == \
           ProductDetailsPageSelectMenu.VALUE_ZERO.value.strip()

    prod_details_page \
        .select_option_by_attribute_value(str(random.randrange(1, 5))) \
        .select_option_by_index(0)
