"""Testing scenario with adding product to the cart
without providing required image upload"""
from pages.product_details_page import ProductDetailsPage


def test_add_to_cart_without_upload_file(browser, get_env):
    """"""
    site_url = get_env['environment']['site_url']
    prod_details_page = ProductDetailsPage(browser, site_url)
    prod_details_page.go_to_site()
