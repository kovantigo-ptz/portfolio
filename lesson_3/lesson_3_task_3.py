'''
3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
Например:
>>>  thesaurus("Иван", "Мария", "Петр", "Илья")
{
    "И": ["Иван", "Илья"],
    "М": ["Мария"], "П": ["Петр"]
}
Подумайте: полезен ли будет вам оператор распаковки?
Как поступить, если потребуется сортировка по ключам? Можно ли использовать словарь в этом случае?
'''

#  ----------Вариант 1----------


def thesaurus(*args):
    names_of_employees = {}
    for item in args:
        #  creating a list of names starting with the same letter
        name_values = list(filter(lambda name: name.title().startswith(item[0]), args))
        name_values.sort()
        names_of_employees.setdefault(item[0], name_values)
    #  sorting by name key
    sort_names_of_employees = dict(sorted(names_of_employees.items(), key=(lambda i: i)))
    return sort_names_of_employees


name_list = ['Евдокия', 'Галина', 'Евгений', 'Елена', 'Игорь', 'Анастасия', 'Иван', 'Антон', 'Ксения']

print(thesaurus(*name_list))

#  --------------------------------------------------------------------------------------------------
#  ----------Вариант 2----------


def thesaurus(*args):
    '''
    Convert tuple of names to dict

    :param args: tuple of names
    :return: alphabet sort dict by key
    '''
    names_of_employees = {}
    for item in args:
        #  checking the existence of the name key
        if names_of_employees.get(item[0]):
            names_of_employees[item[0]].append(item)
            names_of_employees[item[0]].sort()
        #  adding new key and value
        else:
            names_of_employees.setdefault(item[0], [item])
    #  sorting by name key
    sort_names_of_employees = dict(sorted(names_of_employees.items(), key=(lambda i: i)))
    return sort_names_of_employees


name_list = ['Евдокия', 'Галина', 'Евгений', 'Елена', 'Игорь', 'Анастасия', 'Иван', 'Антон', 'Ксения']

print(thesaurus(*name_list))
