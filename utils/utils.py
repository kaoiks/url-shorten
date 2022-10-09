import secrets
import string


def create_random_string(num: int):
    random_string = ""
    for x in range(num):
        random_string += secrets.choice(string.ascii_letters + string.digits)
    return random_string

