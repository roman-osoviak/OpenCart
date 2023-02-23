"""
This module describes methods that are using widely through the program
"""
import functools
import random
import string
import time

from faker import Faker


def get_random_string(length: int, case=None):
    """
    Generate random length enough password with letters and digits
    Function has two parameters:
    required LENGTH and optional CASE,
    you can set strength enough password and case that you need

    :param length: provide a length of string you need
    :param case: specify string like 'lower', or 'upper' or
    left blank to create camelCase string
    :return: string
    """
    if case == 'upper':
        letters = string.ascii_uppercase
    elif case == 'lower':
        letters = string.ascii_lowercase
    else:
        letters = string.ascii_letters

    return ''.join(random.choice(letters + string.digits) for i in range(length))


def get_random_email():
    """Function for generating random email value"""
    return Faker().email()


def get_random_first_name():
    """Function for generating random name value"""
    return Faker().first_name()


def get_random_last_name():
    """Function for generating random last name value"""
    return Faker().last_name()


def trim_currency_from_string(string_with_currency: str):
    """
    Method that trims first currency symbol from the string

    :param string_with_currency: provided string
    :return: string without currency sign
    """
    string_without_currency = string_with_currency[1:]
    return string_without_currency


#  Create wait decorator that executes function for X seconds until it returns Y.


def retry(timeout=10, polling=0.2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            end_time = time.time() + timeout
            while True:
                try:
                    return func(*args, **kwargs)
                except Exception as e:  # pylint: disable=W0703
                    if time.time() > end_time:
                        raise AssertionError()
                    time.sleep(polling)

        return wrapper
