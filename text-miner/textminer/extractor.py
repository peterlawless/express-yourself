import re


def phone_numbers(string):
    return re.findall(r'\(\d{3}\)\s\d{3}-\d{4}', string)
