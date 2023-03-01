"""Testing scenario with adding product to the cart
without providing required image upload"""

from pages.product_details_page import ProductDetailsPage
from utils.common import get_random_choice
from utils.enums import ProductDetailsPageRadio, ProductDetailsPageCheckBox, \
    ProductDetailsPageSelectMenu


def test_add_to_cart_without_upload_file(browser, get_env):
    """Test adding product to the cart flow and without uploaded file"""

    site_url = get_env['environment']['site_url']
    prod_details_page = ProductDetailsPage(browser, site_url)
    prod_details_page.go_to_site()

    prod_details_page.click_on_radio_button(get_random_choice(ProductDetailsPageRadio))
    prod_details_page.click_on_checkbox(get_random_choice(ProductDetailsPageCheckBox))

    prod_details_page.set_random_string_to_text_input(4)
    prod_details_page.select_dropdown_option(
        ProductDetailsPageSelectMenu.random_with_exclude(ProductDetailsPageSelectMenu,
                                                         ProductDetailsPageSelectMenu.VALUE_ZERO))
    prod_details_page.set_random_string_to_textarea(4)
    prod_details_page.click_on_add_to_cart_button()
    prod_details_page.verify_file_required_error_is_displayed()
