import random
import string

def get_random_password() -> str:
    password_length = 8
    possible_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    password = random.sample(possible_chars, password_length)
    new_password_str = "".join(password)
    return new_password_str

print(get_random_password())
