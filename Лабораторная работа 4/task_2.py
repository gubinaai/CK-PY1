my_dict = {}  # создаю пустой словарь

def get_count_char(str_):  # функция для создания my_dict
    str_ = str_.lower()
    for letter in str_:
        if letter.isalpha():
            if letter in my_dict:
                my_dict[letter] += 1
            else:
                my_dict[letter] = 1
    return my_dict

def get_percent_char(dict_):  # фунция для создания словаря с процентами
    new_dict = {}
    summary = sum(dict_.values())
    for key, value in dict_.items():
        new_dict[key] = round((value / summary) * 100, 2)
    return new_dict

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print(get_count_char(main_str))
print(get_percent_char(my_dict))
