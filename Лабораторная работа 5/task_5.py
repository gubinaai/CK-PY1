import random
import string

n = 8  # кол-во символов
def get_random_password() -> str:
    possible_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    password = random.sample(possible_chars, n)
    new_password_str = "".join(password)
    return new_password_str

print(get_random_password())
