'''
2. Дан список:
['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками
(добавить кавычку до и кавычку после элемента списка, являющегося числом)
и дополнить нулём до двух целочисленных разрядов:

Сформировать из обработанного списка строку:
в "05" часов "17" минут температура воздуха была "+05" градусов
'''

weather = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for item in weather:
    if len(item) == 2 and item.replace('+', '').replace('-', '').isdigit() and item[0] in '+-':
        weather[weather.index(item)] = f'"{item[0]}0{item[-1]}"'
    elif len(item) == 1 and item.isdigit():
        weather[weather.index(item)] = f'"0{item}"'
    elif item.replace('+', '').replace('-', '').isdigit():
        weather[weather.index(item)] = f'"{item}"'
print(' '.join(weather))