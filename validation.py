import re


def validation(password):
    """
    13. написати функцію, яка перевіряє пароль на відповідність
    правилам:
    """
    if all([re.findall(r'[a-z]+', password), re.findall(r'[0-9]+', password),
            re.findall(r'[A-Z]+', password), re.findall(r'[$#@]+', password),
            6 <= len(password) <= 12]):
        return True
    else:
        return False
