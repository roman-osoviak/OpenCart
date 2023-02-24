"""Test module devoted to text input field"""
from pages.product_details_page import ProductDetailsPage
from utils.enums import ProductDetailsPageCaptions


def test_user_can_input_text(browser, get_env):
    """Check user input"""
    site_url = get_env['environment']['site_url']
    prod_details_page = ProductDetailsPage(browser, site_url)
    prod_details_page.go_to_site()

    # check default value of input
    assert prod_details_page.get_text_input_attribute_value() \
           == ProductDetailsPageCaptions.TEXT_INPUT_DEFAULT_VALUE.value
    # check placeholder value
    assert prod_details_page.get_text_input_attribute_placeholder() \
           == ProductDetailsPageCaptions.TEXT_PLACEHOLDER.value

    prod_details_page.set_random_string_to_text_input()
    assert not prod_details_page.get_text_input_attribute_value() \
               == ProductDetailsPageCaptions.TEXT_INPUT_DEFAULT_VALUE.value
