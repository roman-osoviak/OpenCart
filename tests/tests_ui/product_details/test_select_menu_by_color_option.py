"""Verifying select drop-down menu by desired color"""
from pages.product_details_page import ProductDetailsPage
from utils.enums import ProductDetailsPageSelectMenu


def test_select_option_by_color(browser, get_env):
    """Test drop-down"""
    site_url = get_env['environment']['site_url']
    prod_details_page = ProductDetailsPage(browser, site_url)
    prod_details_page.go_to_site()

    prod_details_page.select_option_by_desired_color(
        ProductDetailsPageSelectMenu.VALUE_FOURTH_RED.value[1])

    prod_details_page.select_option_by_desired_color(
        ProductDetailsPageSelectMenu.VALUE_THIRD_BLUE.value[1])

    prod_details_page.select_option_by_desired_color(
        ProductDetailsPageSelectMenu.VALUE_FIRST_GREEN.value[1])

    prod_details_page.select_option_by_desired_color(
        ProductDetailsPageSelectMenu.VALUE_SECOND_YELLOW.value[1])
