import random

list_length = 15
from_range = -10
to_range = 10
def get_unique_list_numbers() -> list[int]:
    list_unique_numbers = []
    while len(list_unique_numbers) != list_length:
        number = random.randrange(from_range, to_range)
        if number not in list_unique_numbers:
            list_unique_numbers.append(number)
    return list_unique_numbers

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
