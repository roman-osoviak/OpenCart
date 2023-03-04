"""Module for testing date element"""
import allure

from pages.product_details_page import ProductDetailsPage
from utils.common import fake


def test_date_selection(browser, get_env):
    """Positive date selection case"""
    site_url = get_env['environment']['site_url']

    with allure.step(f'Opening {site_url}'):
        prod_details_page = ProductDetailsPage(browser, site_url)
        prod_details_page.go_to_site()

    with allure.step('Select date'):
        prod_details_page.click_and_select_date_input(fake.date())
        prod_details_page.select_time(fake.time())
        prod_details_page.select_date_time(fake.date_time())
