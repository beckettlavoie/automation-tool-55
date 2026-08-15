import re

def validate_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(email_regex, email))


def validate_url(url):
    url_regex = r'^(http|https)://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}.*$'
    return bool(re.match(url_regex, url))


def validate_integer(value):
    return isinstance(value, int) 


def validate_float(value):
    return isinstance(value, float) 


def validate_positive_integer(value):
    return validate_integer(value) and value > 0


def validate_positive_float(value):
    return validate_float(value) and value > 0.0