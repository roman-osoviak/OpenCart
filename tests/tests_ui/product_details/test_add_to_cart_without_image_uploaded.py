"""Testing scenario with adding product to the cart
without providing required image upload"""

from pages.product_details_page import ProductDetailsPage
from utils.common import get_random_choice
from utils.enums import ProductDetailsPageRadio, ProductDetailsPageCheckBox, ProductDetailsPageSelectMenu


def test_add_to_cart_without_upload_file(browser, get_env):
    """Test adding product to the cart flow and without uploaded file"""
    site_url = get_env['environment']['site_url']
    prod_details_page = ProductDetailsPage(browser, site_url)
    prod_details_page.go_to_site()

    # prod_details_page.click_on_upload_button()
    prod_details_page.click_on_radio_button(get_random_choice(ProductDetailsPageRadio))
    prod_details_page.click_on_checkbox(get_random_choice(ProductDetailsPageCheckBox))
    prod_details_page.set_random_string_to_text_input()
    prod_details_page.select_dropdown_option(get_random_choice(ProductDetailsPageSelectMenu).value[1])
    # to do: bad case with 'Please Select'
