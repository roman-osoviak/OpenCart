"""Testing scenario with adding product to the cart
without providing required image upload"""

from pages.product_details_page import ProductDetailsPage
from utils.common import get_random_choice
from utils.enums import ProductDetailsPageRadio


def test_add_to_cart_without_upload_file(browser, get_env):
    """Test adding product to the cart flow and without uploaded file"""
    site_url = get_env['environment']['site_url']
    prod_details_page = ProductDetailsPage(browser, site_url)
    prod_details_page.go_to_site()

    # prod_details_page.click_on_upload_button()
    prod_details_page.click_on_radio_button(get_random_choice(ProductDetailsPageRadio))
    # to do
