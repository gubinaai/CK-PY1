import random

def get_unique_list_numbers() -> list[int]:
    list_unique_numbers = []
    while len(list_unique_numbers) != 15:
        number = random.randrange(-10, 10)
        if number not in list_unique_numbers:
            list_unique_numbers.append(number)
    return list_unique_numbers

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
