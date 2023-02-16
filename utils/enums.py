"""Module with enumerates"""

from enum import Enum


class BrowserDefinition(Enum):
    """Browser's class definition"""
    CHROME = 'chrome'
    FIREFOX = 'firefox'
    SAFARI = 'safari'
    EDGE = 'edge'


class RegPageErrorType(Enum):
    """IDs of error text in Registration page"""
    FIRST_NAME = "input-firstname"
    LAST_NAME = "input-lastname"
    EMAIL = "input-email"
    PHONE = "input-telephone"
    PASSWORD = "input-password"
    CONFIRM_PASSWORD = "input-confirm"


class StoreCurrency(Enum):
    """Default text for all currencies"""
    SHOPPING_CART_BUTTON_ZERO_COST_USD = '0 item(s) - $0.00'
    SHOPPING_CART_BUTTON_ZERO_COST_EURO = '0 item(s) - 0.00€'
    SHOPPING_CART_BUTTON_ZERO_COST_POUND = '0 item(s) - £0.00'


class Currency(Enum):
    """Store currencies"""
    USD = 'USD', '$'
    EURO = 'EURO', '€'
    POUNDS = 'POUND STERLING', '£'


class ProductDetailsPageRadio(Enum):
    """Class describes radio elements on Product Details page"""
    RADIO_OPTION_FIRST = "Small"
    RADIO_OPTION_SECOND = "Medium"
    RADIO_OPTION_THIRD = "Large"


class ProductDetailsPageCheckBox(Enum):
    """Class describes check-box elements on Product Details page"""
    CHECKBOX_LABEL = "Checkbox"
    CHECKBOX_OPTION_FIRST = "Checkbox 1 (+$14.00)"
    CHECKBOX_OPTION_SECOND = "Checkbox 2 (+$26.00)"
    CHECKBOX_OPTION_THIRD = "Checkbox 3 (+$38.00)"
    CHECKBOX_OPTION_FOURTH = "Checkbox 4 (+$50.00)"


class ProductDetailsPageCaptions(Enum):
    TEXT_PLACEHOLDER = "Text"
    TEXT_INPUT_DEFAULT_VALUE = "test"


class ProductDetailsPageSelectMenu(Enum):
    """Class describes select drop-down elements on Product Details page"""
    SELECT_LABEL = "Select"
    SELECT_DEFAULT_PLACEHOLDER = " --- Please Select --- "
    SELECT_OPTION_FIRST = "Green (+$3.20)"
    SELECT_OPTION_SECOND = "Yellow (+$4.40)"
    SELECT_OPTION_THIRD = "Blue (+$5.60)"
    SELECT_OPTION_FOURTH = "Red (+$6.80)"
