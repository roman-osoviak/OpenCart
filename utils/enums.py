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
