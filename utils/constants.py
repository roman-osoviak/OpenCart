"""For storing common constants"""


# pylint: disable=too-few-public-methods
class ForgotPasswordPageWarning:
    """Common warnings on the Login page"""
    EMAIL_NOT_FOUND = ' Warning: The E-Mail Address was not found in our records!'


class PageTitle:
    """Titles of each page"""
    LOGIN_PAGE_TITLE = 'Account Login'
    MY_ACCOUNT_PAGE_TITLE = 'My Account'
    REGISTRATION_PAGE_TITLE = 'Register Account'
    REGISTERED_PAGE_TITLE = 'Your Account Has Been Created!'
    FORGOT_PASSWORD_PAGE_TITLE = 'Forgot Your Password?'
    FORGOT_PASSWORD_SUCCESS = 'Your Password Was Restored'
    SHOPPING_CART_PAGE_TITLE = 'Your Store'


# pylint: disable=too-few-public-methods
class RegPageError:
    """Error text class"""
    BAD_FIRST_NAME = 'First Name must be between 1 and 32 characters!'
    BAD_LAST_NAME = 'Last Name must be between 1 and 32 characters!'
    BAD_EMAIL = 'E-Mail Address does not appear to be valid!'
    BAD_TELEPHONE = 'Telephone must be between 3 and 32 characters!'
    BAD_PASSWORD = 'Password must be between 4 and 20 characters!'
    PASSWORD_MISMATCH = 'Password confirmation does not match password!'


class StoreItems:
    """  Captions from Store Page """
    SHOPPING_CART_DROPDOWN_EMPTY_TEXT = 'Your shopping cart is empty!'
    SHOPPING_CART_BUTTON_ZERO_COST = '0 item(s) - $0.00'
