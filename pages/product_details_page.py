"""
This module describes Product's Details Page
"""
import logging
from enum import Enum

from hamcrest import assert_that, equal_to
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from locators.product_details_locators import DescriptionLocators, \
    ProductDetailsLocators, SpecificationLocators, ReviewsLocators
from pages.base_page import BasePage
from utils.common import retry
from utils.common import trim_currency_from_string, get_random_string
from utils.enums import ProductDetailsPageRadio, ProductDetailsPageCheckBox, \
    ProductDetailsPageSelectMenu, ProductDetailsTextarea, ProductDetailsTabsLower


class _DescriptionTab:
    """Describes Description Tab"""

    def __init__(self):
        """Constructor"""
        self.description_instance = DescriptionLocators()


class ProductDetailsAttributes(Enum):
    """Class describes attribute names"""
    ATTRIBUTE_PLACEHOLDER = 'placeholder'
    ATTRIBUTE_VALUE = 'value'
    ATTRIBUTE_TEXT = 'text'


# pylint: disable=too-many-public-methods
class ProductDetailsPage(BasePage):
    """Class for Product's Details Page"""
    _URL_PATH = '?route=product/product&language=en-gb&product_id=42'

    def go_to_site(self):
        """Open details page"""
        return self.driver.get(self.base_url + self._URL_PATH)

    def click_on_add_wish_button(self):
        """Method that clicks on Wish btn"""
        self.click_on_element(ProductDetailsLocators.ADD_TO_WISH_LIST_BUTTON)

    def click_on_add_compare_button(self):
        """Method that clicks on add to compare list"""
        self.click_on_element(ProductDetailsLocators.ADD_TO_COMPARE_BUTTON)

    def click_on_brand(self):
        """Method clicks on Apple brand link"""
        self.click_on_element(ProductDetailsLocators.BRAND_APPLE_LINK)

    def click_on_text_field(self):
        """
        Clicking on text field

        :return: None
        """
        self.find_element(ProductDetailsLocators.TEXT_INPUT).click()

    @retry(10)
    def click_on_upload_button(self):
        """
        Method clicks on upload button

        :return: None
        """
        self.find_element(ProductDetailsLocators.BUTTON).click()
        upload_file = self.find_element(ProductDetailsLocators.UPLOAD_FILE_DIALOG)
        upload_file.send_keys("/home/administrator/requirements_12_febr")

    def verify_old_price_is_greater_than_new(self):
        """
        Verifying that new price is lower than old one

        :return: True, otherwise False
        """
        old_price = float(trim_currency_from_string(
            self.get_element_text(ProductDetailsLocators.OLD_PRICE)))
        new_price = float(trim_currency_from_string(
            self.get_element_text(ProductDetailsLocators.NEW_PRICE)))
        return old_price > new_price

    def get_alert_text(self):
        """
        Method returns alert's text value

        :return: alert's text
        """

        return self.get_element_text(ProductDetailsLocators.TOP_ALERT)

    def get_text_input_attribute_text(self):
        """
        Method that retrieve input field text

        :return: input's text
        """
        return self.get_element_text(ProductDetailsLocators.TEXT_INPUT)

    def get_text_input_attribute_placeholder(self):
        """
        Method that retrieve placeholder input field

        :return: input's text
        """
        return self.get_element_attribute(ProductDetailsLocators.TEXT_INPUT,
                                          ProductDetailsAttributes.ATTRIBUTE_PLACEHOLDER)

    def get_textarea_attribute_placeholder(self):
        """
        Method that retrieve textarea placeholder

        :return: textarea placeholder
        """
        return self.get_element_attribute(ProductDetailsLocators.TEXT_AREA,
                                          ProductDetailsAttributes.ATTRIBUTE_PLACEHOLDER)

    def verify_textarea_placeholder(self):
        """Method verifying placeholder text"""
        assert_that(self.get_textarea_attribute_placeholder(),
                    equal_to(ProductDetailsTextarea.PLACEHOLDER.value))

    def get_textarea_attribute_text(self):
        """
        Method that returns text from Textarea element

        :return: Text from Textarea element
        """
        return self.get_element_text(ProductDetailsLocators.TEXT_INPUT)

    def get_text_input_attribute_value(self):
        """
        Returns attribute value for text input element

        :return: string
        """
        return self.get_element_attribute(ProductDetailsLocators.TEXT_INPUT,
                                          ProductDetailsAttributes.ATTRIBUTE_VALUE)

    def get_radio_text_attribute_value(self, radio_btn_option: ProductDetailsPageRadio):
        """
        Method that returns text from element

        :param radio_btn_option:
        :return:
        """
        return self.get_element_text(
            ProductDetailsLocators.RADIO_OPTIONS_LABELS(radio_btn_option.value))

    def select_option_by_attribute_value(self, value: str = '0'):
        """Method that selects drop-down option by value"""
        select = Select(self.find_element(ProductDetailsLocators.SELECT_MENU_DROPDOWN))
        select.select_by_value(value)

    def select_option_by_visible_text(self, text: str):
        """Method selects drop-down option by visible text"""
        select = Select(self.find_element(ProductDetailsLocators.SELECT_MENU_DROPDOWN))
        select.select_by_visible_text(text)

    def select_option_by_index(self, index: int):
        """Method selects drop-down option by index"""
        select = Select(self.find_element(ProductDetailsLocators.SELECT_MENU_DROPDOWN))
        select.select_by_index(index)
        return self

    def select_dropdown_option(self, text: ProductDetailsPageSelectMenu):
        """Method selects drop-down option by index"""
        value = self.find_element(
            ProductDetailsLocators.SELECT_MENU_DROPDOWN_ITEM(
                text)).get_attribute('value')
        select = Select(self.find_element(ProductDetailsLocators.SELECT_MENU_DROPDOWN))
        select.select_by_value(value)
        return self

    def select_option_by_text_color(self, color_option: ProductDetailsPageSelectMenu):
        """Method selects drop-down option by provided color"""
        select = Select(self.find_element(ProductDetailsLocators.SELECT_MENU_DROPDOWN))

        # creating a list with visible text from select options
        new_list = [element.text for element in select.options]

        for i in new_list:
            index = i.find(color_option)
            if index != -1:
                select.select_by_visible_text(i)
                break

    def get_selected_option_text_from_select(self):
        """
        Function returns currently selected option text

        :return: text of the preselected option
        """
        select = Select(self.find_element(ProductDetailsLocators.SELECT_MENU_DROPDOWN))
        return select.first_selected_option.text

    def verify_alert_is_displayed(self, is_displayed: bool = True):
        """
        Check if our alert element is shown

        :return: True if success, otherwise None
        """
        if is_displayed:
            assert self.is_element_displayed(ProductDetailsLocators.MUST_TO_LOGIN_WISH_LIST)
        else:
            assert self.is_element_invisible(ProductDetailsLocators.MUST_TO_LOGIN_WISH_LIST)
        return self

    def verify_file_required_error_is_displayed(self, is_displayed: bool = True):
        """
        Method checks that file required error is shown
        """
        if is_displayed:
            self.is_element_displayed(ProductDetailsLocators.BUTTON_REQUIRED_ERROR)
        else:
            self.is_element_invisible(ProductDetailsLocators.BUTTON_REQUIRED_ERROR)
        return self

    def verify_text_required_error_is_displayed(self, is_displayed: bool = True):
        """Method checks that error about required text is shown"""
        if is_displayed:
            self.is_element_displayed(ProductDetailsLocators.TEXT_INPUT_REQUIRED_ERROR)
        else:
            self.is_element_invisible(ProductDetailsLocators.TEXT_INPUT_REQUIRED_ERROR)
        return self

    def verify_select_required_error_is_displayed(self, is_displayed: bool = True):
        """Method checks that error about required select is shown"""
        if is_displayed:
            self.is_element_displayed(ProductDetailsLocators.SELECT_REQUIRED_ERROR)
        else:
            self.is_element_invisible(ProductDetailsLocators.SELECT_REQUIRED_ERROR)
        return self

    def verify_textarea_required_error_is_displayed(self, is_displayed: bool = True):
        """Method checks that error about required textarea is shown"""
        if is_displayed:
            self.is_element_displayed(ProductDetailsLocators.TEXT_AREA_REQUIRED_ERROR)
        else:
            self.is_element_invisible(ProductDetailsLocators.TEXT_AREA_REQUIRED_ERROR)
        return self

    def verify_radio_required_error_is_displayed(self, is_displayed: bool = True):
        """Method checks that error about required radio is shown"""
        if is_displayed:
            assert self.is_element_displayed(ProductDetailsLocators.RADIO_REQUIRED_ERROR)
        else:
            assert self.is_element_invisible(ProductDetailsLocators.RADIO_REQUIRED_ERROR)
        return self

    def verify_checkbox_required_error_is_displayed(self, is_displayed: bool = True):
        """Method checks that error about required checkbox is shown"""
        if is_displayed:
            self.is_element_displayed(ProductDetailsLocators.CHECKBOX_REQUIRED_TEXT)
        else:
            self.is_element_invisible(ProductDetailsLocators.CHECKBOX_REQUIRED_TEXT)
        return self

    def verify_tab_is_active(self, tab: ProductDetailsTabsLower):
        """Checks if tab is currently active"""
        if tab == ProductDetailsTabsLower.TAB_SPECIFICATION:
            class_value = self.get_element_attribute(SpecificationLocators.TAB_SPECIFICATION,
                                                     'class')
        elif tab == ProductDetailsTabsLower.TAB_DESCRIPTION:
            class_value = self.get_element_attribute(DescriptionLocators.TAB_DESCRIPTION,
                                                     'class')
        else:
            class_value = self.get_element_attribute(ReviewsLocators.TAB_REVIEWS,
                                                     'class')
        assert 'active' in class_value
        return self

    def set_random_string_to_text_input(self, text_length: int):
        """
        Generate string of desired length and inputs it into text field

        :param text_length: text length
        :return: None
        """
        self.type_text_in_ui_element(ProductDetailsLocators.TEXT_INPUT,
                                     get_random_string(text_length))

    def set_random_string_to_textarea(self, text_length: int):
        """
        Inputs string of desired length into text area element

        :param text_length: text length
        :return: None
        """
        self.type_text_in_ui_element(ProductDetailsLocators.TEXT_AREA,
                                     get_random_string(text_length))

    def click_on_radio_button(self, radio_btn_option: ProductDetailsPageRadio):
        """
        Method that selects desired radio-button

        :return: self
        """
        self.find_element(ProductDetailsLocators.RADIO_BUTTON(radio_btn_option.value)).click()
        return self

    def click_on_checkbox(self, checkbox_btn_option: ProductDetailsPageCheckBox,
                          select: bool = True):
        """
        Method that clicks on desired checkbox option

        :param checkbox_btn_option: checkbox option we want to deal
        :param select: True if we need to select option, False otherwise
        :return: self
        """
        self._trigger_checkbox(ProductDetailsLocators.CHECKBOX_BUTTON(checkbox_btn_option.value),
                               select)
        return self

    def click_and_select_date_input(self, date, change_time: bool = True):
        """Method clicks on date input and type desired date"""
        if change_time:
            logging.info("Trying to input date as '%s'", date)
            self.type_text_in_ui_element(ProductDetailsLocators.DATE_INPUT, date)
            logging.info("Date provided successfully")
            self.find_element(ProductDetailsLocators.DATE_INPUT).send_keys(Keys.ESCAPE)
        else:
            logging.info("Time was not provided by test choice")
        return self

    @retry(10)
    def select_time(self, time, change_time: bool = True):
        """
        Method provides random time into time input and click Apply btn if needed
        :param time: random time
        :param change_time: True if we desire to change time, otherwise False
        :return: None
        """
        if change_time:
            logging.info("Trying to input time as '%s'", time)
            self.type_text_in_ui_element(ProductDetailsLocators.TIME_INPUT, time)
            logging.info("Time provided successfully")
            self.click_on_element(ProductDetailsLocators.APPLY_EXPANDED_BUTTON)
        else:
            logging.info("Time was not provided by test choice")
        return self

    def select_date_time(self, datetime, change_time: bool = True):
        """
        Method provides random datetime into datetime input and click Apply btn if needed
        :param datetime: random time
        :param change_time: True if we desire to change time, otherwise False
        :return: None
        """
        if change_time:
            logging.info("Trying to input datetime as '%s'", datetime)
            self.type_text_in_ui_element(ProductDetailsLocators.DATE_TIME_INPUT,
                                         str(datetime))
            logging.info("Datetime provided successfully")
            self.click_on_element(ProductDetailsLocators.APPLY_EXPANDED_BUTTON)
        else:
            logging.info("Datetime was not provided by test choice")
        return self

    def verify_checkbox_is_selected(self, checkbox_btn_option: ProductDetailsPageCheckBox,
                                    is_selected: bool = True):
        """
        Method for clicking on checkbox options

        :param checkbox_btn_option: checkbox option we should work
        :param is_selected: True if we need to check that flag is selected, False otherwise
        :return: if True we expect to be selected, False otherwise
        """
        if is_selected:
            self.is_element_selected(
                ProductDetailsLocators.CHECKBOX_BUTTON(checkbox_btn_option.value))
        else:
            self.is_element_not_selected(
                ProductDetailsLocators.CHECKBOX_BUTTON(checkbox_btn_option.value))
        return self

    def verify_radio_button_is_selected(self, radio_btn_option: ProductDetailsPageRadio,
                                        is_selected: bool = True) -> object:
        """
        Method that checks if radio button is selected

        :param radio_btn_option: radio option
        :param is_selected: desired state True/False
        :return: self
        """
        if is_selected:
            self.is_element_selected(ProductDetailsLocators.RADIO_BUTTON(radio_btn_option.value))
        else:
            self.is_element_not_selected(
                ProductDetailsLocators.RADIO_BUTTON(radio_btn_option.value))
        return self

    def verify_radio_button_label(self, radio_btn_option: ProductDetailsPageRadio, label: str):
        """
        Method checks if label is equal to our expectations

        :param radio_btn_option: Option with desired value
        :param label: label text
        :return: True if equal, otherwise False
        """
        assert self.get_element_text(
            ProductDetailsLocators.RADIO_OPTIONS_LABELS(radio_btn_option.value)) == label

    def click_on_add_to_cart_button(self):
        """
        Method clicks on "Add to Cart" button
        :return: self
        """
        self.click_on_element(ProductDetailsLocators.BUTTON_ADD_TO_CART)
        return self

    def click_on_tab_lower(self, tab: ProductDetailsTabsLower):
        """Method for clicking on lower tab"""
        if tab == ProductDetailsTabsLower.TAB_DESCRIPTION:
            self.click_on_element(DescriptionLocators.TAB_DESCRIPTION)
        elif tab == ProductDetailsTabsLower.TAB_SPECIFICATION:
            self.click_on_element(SpecificationLocators.TAB_SPECIFICATION)
        else:
            self.click_on_element(ReviewsLocators.TAB_REVIEWS)
        return self
