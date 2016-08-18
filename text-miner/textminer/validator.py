import re


def binary(string):
    match = re.search(r'^[01]+$', string)
    return bool(match)


def binary_even(string):
    match = re.search(r'^[01]+[0]$', string)
    return bool(match)


def hex(string):
    match = re.search(r'^[A-F0-9]+$', string)
    return bool(match)


def word(string):
    match = re.search(r'^[A-Za-z0-9]*-?[A-Za-z]+$', string)
    return bool(match)


def words(string, count=None):
    breakout = re.findall(r'\b[A-Za-z0-9]*-?[A-Za-z]\b', string)
    if count and breakout:
        return len(breakout) == count
    return bool(breakout)


def phone_number(string):
    match = re.search(r'^\(?\d{3}\)?[-\.\s]?\d{3}[-\.\s]?\d{4}$', string)
    return bool(match)


def money(string):
    match = re.search(r'^\$[0-9]{1,3}(?:,?[0-9]{3})*(?:\.[0-9]{2})?$', string)
    return bool(match)


def zipcode(string):
    match = re.search(r'^[0-9]{5}(?:-[0-9]{4})?$', string)
    return bool(match)


def date(string):
    match = re.search(r'\d{1,2}/\d{1,2}/\d{4}|\d{4}-\d{2}-\d{2}', string)
    return bool(match)
