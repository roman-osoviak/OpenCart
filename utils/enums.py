"""Module with enumerates"""

from enum import Enum


class BrowserDefinition(Enum):
    """Browser's class definition"""
    CHROME = 'chrome'
    FIREFOX = 'firefox'
    SAFARI = 'safari'
    EDGE = 'edge'
