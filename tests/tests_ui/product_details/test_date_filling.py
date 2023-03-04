"""Module for testing date element"""
from pages.product_details_page import ProductDetailsPage
from utils.common import get_random_date, get_random_time, get_random_datetime


def test_date_selection(browser, get_env):
    """Positive date selection case"""
    site_url = get_env['environment']['site_url']
    prod_details_page = ProductDetailsPage(browser, site_url)
    prod_details_page.go_to_site()

    prod_details_page.click_and_select_date_input(get_random_date())
    prod_details_page.select_time(get_random_time())
    prod_details_page.select_date_time(get_random_datetime())
