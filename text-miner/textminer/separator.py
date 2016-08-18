import re


def words(string):
    match = re.findall(r'\b(?:[A-Za-z]*|[0-9]*)-?[A-Za-z]+\b', string)
    if len(match) == 0:
        return None
    else:
        return match


def phone_number(string):
    match = re.search(r'\(?(\d{3})\)?[-\.\s]?(\d{3})[-\.\s]?(\d{4})', string)
    if match:
        area_code, first_three, last_four = match.groups()
        number = "{}-{}".format(first_three, last_four)
        number_dict = {"area_code": area_code, "number": number}
        return number_dict


def money(string):
    match = re.search(r'^\$([0-9]{1,3})(?:,?([0-9]{3}))?(?:,?([0-9]{3}))?(?:(\.[0-9]{2}))?$', string)
    return_string = ''
    if match:
        for element in match.groups():
            return_string += element
        return {"currency": "$", "amount": float(return_string)}


def zipcode(string):
    match = re.search(r'^(\d{5})(?:-?(\d{4}))?$', string)
    if match:
        code, plus4 = match.groups()
        return {"zip": code, "plus4": plus4}


def date(string):
    match_one = re.search(r'(\d{1,2})/(\d{1,2})/(\d{4})', string)
    match_two = re.search(r'(\d{4})-(\d{2})-(\d{2})', string)
    if match_one:
        month, day, year = match_one.groups()
    elif match_two:
        year, month, day = match_two.groups()
    else:
        return None
    return {"month": int(month), "day": int(day), "year": int(year)}
