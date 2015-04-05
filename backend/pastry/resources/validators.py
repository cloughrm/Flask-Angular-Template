def email_address(value, name):
    if '@' not in value or '.' not in value:
        raise ValueError('Username must be a valid email address')
    return value
