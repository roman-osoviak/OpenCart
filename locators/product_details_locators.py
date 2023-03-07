"""Module with locators for Product Details page"""
from selenium.webdriver.common.by import By

from utils.enums import ProductDetailsButton

# pylint: disable=too-few-public-methods
class DescriptionLocators:
    """Locators in Description Tab"""


class SpecificationLocators:
    """Locators in Specification Tab"""


class ReviewsLocators:
    """Locators on Reviews Tab"""


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
    APPLY_EXPANDED_BUTTON = (By.XPATH,
                             '//div[contains(@style, "display: block;")]//../button[text()= "Apply"]')
    CANCEL_EXPANDED_BUTTON = (By.XPATH,
                              '//div[contains(@style, "display: block;")]//../button[text()= "Cancel"]')
    # quantity input
    QUANTITY_INPUT = (By.XPATH, '//*[text()="Qty"]/../input[@name="quantity"]')
    QUANTITY_ALERT = (By.XPATH,
                      '//*[normalize-space(text())="This product has a minimum quantity of 2"]')

    # add to cart button
    BUTTON_ADD_TO_CART = (By.XPATH, '//button[@type="submit" and text() = "Add to Cart"]')
