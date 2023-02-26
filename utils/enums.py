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
    CHECKBOX_OPTION_FIRST = "Checkbox 1"
    CHECKBOX_OPTION_SECOND = "Checkbox 2"
    CHECKBOX_OPTION_THIRD = "Checkbox 3"
    CHECKBOX_OPTION_FOURTH = "Checkbox 4"


class ProductDetailsPageCaptions(Enum):
    """Enum class consists of different placeholders per page"""
    TEXT_PLACEHOLDER = "Text"
    TEXT_INPUT_DEFAULT_VALUE = "test"


class ProductDetailsPageSelectMenu(Enum):
    """Class describes select drop-down elements on Product Details page"""
    VALUE_ZERO = " --- Please Select --- "
    VALUE_FIRST_GREEN = "Green"
    VALUE_SECOND_YELLOW = "Yellow"
    VALUE_THIRD_BLUE = "Blue"
    VALUE_FOURTH_RED = "Red"
