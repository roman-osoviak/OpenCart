"""
This module describes methods that are using widely through the program
"""
import random
import string

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
