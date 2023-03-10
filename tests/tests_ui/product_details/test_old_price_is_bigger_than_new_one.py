"""Module for testing prices"""
import allure
from hamcrest import assert_that

from locators.product_details_locators import ProductDetailsLocators
from pages.product_details_page import ProductDetailsPage
from utils.enums import ColorsInHexString


def test_old_price_is_greater_than_new(browser, get_env):
    """Verify that old price is greater than new one"""
    site_url = get_env['environment']['site_url']
    prod_details_page = ProductDetailsPage(browser, site_url)

    with allure.step(f'Opening {site_url}'):
        prod_details_page.go_to_site()
    with allure.step('Verifying that old price is greater than old one'):
        assert_that(prod_details_page.verify_old_price_is_greater_than_new())
    with allure.step('Verifying correctness of text color for old price'):
        prod_details_page.verify_element_color(ProductDetailsLocators.OLD_PRICE,
                                               ColorsInHexString.ORANGE_COLOR)
