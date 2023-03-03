"""
This module describes methods that are using widely through the program
"""
import random
import string
import time
from random import choice

from faker import Faker

fake = Faker()


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
    return fake.email()


def get_random_first_name():
    """Function for generating random name value"""
    return fake.first_name()


def get_random_last_name():
    """Function for generating random last name value"""
    return fake.last_name()


def get_random_date():
    """Function for generating random date value"""
    return fake.date()


def trim_currency_from_string(string_with_currency: str):
    """
    Method that trims first currency symbol from the string

    :param string_with_currency: provided string
    :return: string without currency sign
    """
    string_without_currency = string_with_currency[1:]
    return string_without_currency


#  Universal solution for all types of exceptions:
#  wait decorator that executes function for X seconds.
def retry(time_out: int):
    """
    Decorator function

    :param time_out: desired time for trying
    :return: decorator func
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            end_time = time.time() + time_out
            while True:
                try:
                    return func(*args, **kwargs)
                except Exception as exception:  # pylint: disable=W0703
                    if time.time() > end_time:
                        raise AssertionError(exception) from None
                    time.sleep(1)

        return wrapper

    return decorator


def get_random_choice(class_choice):
    """
    Method for selection random option from available element options

    :param class_choice:
    :return: one of 'ProductDetailsPageRadio' choice
    """
    return choice(list(class_choice))
