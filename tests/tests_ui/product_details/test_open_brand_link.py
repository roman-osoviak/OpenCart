"""Module for testing clicking on brand link"""

from pages.product_details_page import ProductDetailsPage
from utils.constants import PageTitle


def test_opening_brand_link(browser, get_env):
    """Test brand link"""
    site_url = get_env['environment']['site_url']
    prod_details_page = ProductDetailsPage(browser, site_url)
    prod_details_page.go_to_site()

    assert browser.title == PageTitle.PRODUCT_DETAILS_TITLE

    prod_details_page.click_on_brand()

    assert browser.title == PageTitle.BRAND_PAGE_TITLE
