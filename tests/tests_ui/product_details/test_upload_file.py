"""Module for testing upload file positive flow"""
from pages.product_details_page import ProductDetailsPage


def test_upload_file(browser, get_env):
    """Verifying that file can be uploaded"""
    site_url = get_env['environment']['site_url']
    prod_details_page = ProductDetailsPage(browser, site_url)
    prod_details_page.go_to_site()

    prod_details_page.click_on_upload_button()
