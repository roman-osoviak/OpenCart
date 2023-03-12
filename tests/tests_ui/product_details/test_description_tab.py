"""Module for verifying Description tab"""
import time

import allure

from locators.product_details_locators import DescriptionLocators
from pages.product_details_page import ProductDetailsPage
from utils.enums import ProductDetailsTabsLower


def test_description_tab(browser, get_env, get_project_path):
    """Verifying Description tab method"""
    site_url = get_env['environment']['site_url']
    prod_details_page = ProductDetailsPage(browser, site_url)

    with allure.step(f'Opening {site_url}'):
        prod_details_page.go_to_site()
    prod_details_page.click_on_tab_lower(ProductDetailsTabsLower.TAB_SPECIFICATION)
    prod_details_page.verify_tab_is_active(ProductDetailsTabsLower.TAB_SPECIFICATION)

    prod_details_page.verify_elements_are_not_visible(DescriptionLocators.HEADER_FEATURES,
                                                      DescriptionLocators.HEADER_TECH_SPECIFICATION)

    prod_details_page.click_on_tab_lower(ProductDetailsTabsLower.TAB_DESCRIPTION)
    time.sleep(2)
    # prod_details_page.verify_elements_boldness()
    prod_details_page.verify_inner_text_vs_file_with_dom(DescriptionLocators.TAB_DESCRIPTION_CONTENT,
                                                         get_project_path)
