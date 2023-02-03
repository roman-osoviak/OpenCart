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


class CurrencyTemp(Enum):
    """Store currencies"""
    USD = '$'
    EURO = '€'
    POUNDS = '£'
