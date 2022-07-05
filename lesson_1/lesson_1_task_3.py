'''
3.Склонение слова
Реализовать склонение слова «процент» во фразе «N процентов».
Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:
1 процент
2 процента
3 процента
4 процента
5 процентов
6 процентов
...
100 процентов
'''

category_of_units_1 = [5, 6, 7, 8, 9, 0]
category_of_units_2 = [2, 3, 4]
for number in range(101):
    if number % 10 == 1 and number != 11:
        print(number, 'процент')
    if number % 10 in category_of_units_2 and (number < 12 or number > 14):
        print(number, 'процента')
    if number % 10 in category_of_units_1 or (number >= 11 and number <= 14):
        print(number, 'процентов')
