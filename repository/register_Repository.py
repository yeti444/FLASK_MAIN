import re

def is_password_strong(password):
    return len(password) >= 8 and any(char.isdigit() for char in password) \
        and any(char.isalpha() for char in password) and any(not char.isalnum() for char in password)

def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None