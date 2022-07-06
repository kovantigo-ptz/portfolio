'''
2. Доработать предыдущую функцию в num_translate():
реализовать корректную работу с числительными, начинающимися с заглавной буквы —
результат тоже должен быть с заглавной.
Например:
>>> num_translate_adv("One")
"Один"
>>> num_translate_adv("two")
"два"
'''

def num_translate(numeral):
    if numeral.lower() in numerals and numeral.istitle():
        return numerals.get(numeral.lower()).title()
    else:
        return numerals.get(numeral.lower())

numerals = {'zero': 'нуль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
            'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}

numeral = input('Введите числительное>>')
print(num_translate(numeral))
