"""
This module describes Product's Details Page
"""
from hamcrest import assert_that, equal_to
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
from utils.common import retry
from utils.common import trim_currency_from_string, get_random_string
from utils.enums import ProductDetailsPageRadio, ProductDetailsPageCheckBox, \
    ProductDetailsPageSelectMenu, ProductDetailsTextarea, ProductDetailsButton


# pylint: disable=too-few-public-methods
class ProductDetailsLocators:
    """Locator on Product's Details Page"""
    ADD_TO_WISH_LIST_BUTTON = (
        By.XPATH, '//h1/..//*[@aria-label="Add to Wish List"]')
    ADD_TO_COMPARE_BUTTON = (By.XPATH, '//h1/..//*[@aria-label="Compare this Product"]')
    BRAND_APPLE_LINK = (By.XPATH, '//li[contains(text(), "Brand: ")]//a[text()="Apple"]')
    OLD_PRICE = (By.XPATH, '//*[@class="price-old"]')
    NEW_PRICE = (By.XPATH, '//*[@class="price-new"]')
    TOP_ALERT = (By.XPATH, '//div[@id="alert"]')
    MUST_TO_LOGIN_WISH_LIST = (By.XPATH, '//div[@id="alert"]/div[contains(@class, "alert")]')

    # radio
    # pylint: disable=unnecessary-lambda-assignment
    RADIO_BUTTON = lambda text: (By.XPATH, f'//label[contains(text(), "{text}")]//..//input')
    RADIO_OPTIONS_LABELS = lambda text: \
        (By.XPATH, f'//label[contains(normalize-space(text()), "{text}")]')
    RADIO_LABEL_SMALL = (By.XPATH, '//label[contains(normalize-space(text()), "Small")]')
    RADIO_OPTION_MEDIUM = (By.XPATH, '//label[contains(normalize-space(text()), "Medium")]')
    RADIO_OPTION_LARGE = (By.XPATH, '//label[contains(normalize-space(text()), "Large")]')
    RADIO_REQUIRED_ERROR = (By.XPATH, '//*[starts-with(@id ,"error") and text()="Radio required!"]')

    # checkbox
    CHECKBOX_BUTTON = lambda text: (By.XPATH, f'//label[contains(text(), "{text}")]/..//input')
    CHECKBOX_LABELS_TEXT = lambda text: \
        (By.XPATH, f'//label[contains(normalize-space(text()), "{text}")]')
    CHECKBOX_BUTTON_FIRST = (By.XPATH, '//label[contains(text(), "Checkbox 1")]/../input')
    CHECKBOX_LABEL_FIRST = (By.XPATH,
                            '//label[contains(normalize-space(text()), "Checkbox 1 (+$14.00)")]')
    CHECKBOX_REQUIRED_TEXT = (By.XPATH,
                              '//*[starts-with(@id, "error") and text()="Checkbox required!"]')

    # text input
    TEXT_INPUT = (By.XPATH, '//input[@placeholder="Text"]')
    TEXT_INPUT_REQUIRED_ERROR = (By.XPATH, '//*[text()="Text required!"]')

    # select drop down
    SELECT_MENU_LABEL = (By.XPATH, '//select/../label[contains(text(), "Select")]')
    SELECT_MENU_DROPDOWN = (By.XPATH, '//label[text()="Select"]/../select')
    SELECT_MENU_DROPDOWN_ITEM = lambda text: (By.XPATH,
                                              f'//label[text()="Select"]/../select/option[normalize-space(text())="{text}"]')
    SELECT_FOURTH_OPTION = (By.XPATH, '//option[contains(text(), "Red")]')
    SELECT_REQUIRED_ERROR = (By.XPATH,
                             '//*[starts-with(@id, "error") and text()="Select required!"]')

    # textarea
    TEXT_AREA = (By.XPATH, '//textarea[@placeholder="Textarea"]')
    TEXT_AREA_REQUIRED_ERROR = (By.XPATH,
                                '//*[starts-with(@id, "error") and text()="Textarea required!"]')

    # file upload
    BUTTON_LABEL = (By.XPATH, '//label[contains(text(), "File")]')
    BUTTON = (By.XPATH, '//button[contains(text(), " Upload File")]')
    BUTTON_REQUIRED_ERROR = \
        (By.XPATH, f'//*[contains(text(), "{ProductDetailsButton.ERROR_FILE_REQUIRED.value}")]')
    BUTTON_MAX_SIZE_WARNING = \
        (By.XPATH,
         f'//button[@data-oc-size-error="{ProductDetailsButton.WARNING_MAX_SIZE}"]')
    UPLOAD_FILE_DIALOG = (By.XPATH, '//input[@type="file"]')

    # date time
    DATE_INPUT = (By.XPATH, '//label[text()="Date"]/..//input[contains(@class, "date")]')
    DATE_PICKER = (By.XPATH, '//div[contains(@class, "daterangepicker")]')
    TIME_INPUT = (By.XPATH, '//label[text()="Time"]/..//input[contains(@class, "time")]')
    DATE_TIME_INPUT = (By.XPATH,
                       '//label[text()="Date & Time"]/..//input[contains(@class, "datetime")]')
    # quantity input
    QUANTITY_INPUT = (By.XPATH, '//*[text()="Qty"]/../input[@name="quantity"]')
    QUANTITY_ALERT = (By.XPATH,
                      '//*[normalize-space(text())="This product has a minimum quantity of 2"]')

    # add to cart button
    BUTTON_ADD_TO_CART = (By.XPATH, '//button[@type="submit" and text() = "Add to Cart"]')


class ProductDetailsAttributes:
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

    @retry(10)
    def click_and_select_date_input(self, date):
        """Method clicks on date input and type desired date"""
        origin = self.find_element(ProductDetailsLocators.DATE_INPUT)
        self.type_text_in_ui_element(ProductDetailsLocators.DATE_INPUT, date)
        origin.click()

    @retry(10)
    def click_and_select_time_input(self, time):
        """Method clicks on time input and type desired time"""
        origin = self.find_element(ProductDetailsLocators.TIME_INPUT)
        self.type_text_in_ui_element(ProductDetailsLocators.TIME_INPUT, time)
        origin.click()

    def click_and_select_date_and_time_input(self, datetime):
        """Method clicks on datetime input and type desired datetime"""
        origin = self.find_element(ProductDetailsLocators.DATE_TIME_INPUT)
        self.type_text_in_ui_element(ProductDetailsLocators.DATE_TIME_INPUT,
                                     str(datetime))
        origin.click()

    def click_on_add_to_cart_button(self):
        """
        Method clicks on "Add to Cart" button
        :return: self
        """
        self.click_on_element(ProductDetailsLocators.BUTTON_ADD_TO_CART)
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
