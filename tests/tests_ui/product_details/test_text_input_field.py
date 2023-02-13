"""Test module devoted to text input field"""
from pages.product_details_page import ProductDetailsPage, ProductDetailsAttributes


def test_placeholder_deletes_after_user_input(browser, get_env):
    """Check user input"""
    site_url = get_env['environment']['site_url']
    prod_details_page = ProductDetailsPage(browser, site_url)
    prod_details_page.go_to_site()

    # verify default placeholder
    assert prod_details_page.get_attribute_placeholder() == 'Text'
    prod_details_page.click_on_text_field()
    prod_details_page.set_random_string_to_text_input()
