'''
1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
до минуты: <s> сек;
до часа: <m> мин <s> сек;
до суток: <h> час <m> мин <s> сек;
* в остальных случаях: <d> дн <h> час <m> мин <s> сек.
Примеры:
duration = 53
53 сек
duration = 153
2 мин 33 сек
duration = 4153
1 час 9 мин 13 сек
duration = 400153
4 дн 15 час 9 мин 13 сек
'''

duration = int(input('Введите время в секундах>>'))

SEC_IN_DAY = 86400
SEC_IN_HOUR = 3600
SEC_IN_MIN = 60

time = []
time_name = ['дн', 'час', 'мин', 'сек']

days = duration // SEC_IN_DAY
time.append(days)
duration -= days * SEC_IN_DAY
hours = duration // SEC_IN_HOUR
time.append(hours)
duration -= hours * SEC_IN_HOUR
minutes = duration // SEC_IN_MIN
time.append(minutes)
seconds = duration - (minutes * SEC_IN_MIN)
time.append(seconds)

for index in range(len(time)):
    if time[index] > 0:
        print(time[index], time_name[index], end=' ')
