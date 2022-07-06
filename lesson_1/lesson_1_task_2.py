'''
2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
Внимание: использовать только арифметические операции!
'''

def sum_of_digits(number):
    sum_digits = 0
    while number > 0:
        sum_digits += (number % 10)
        number //= 10
    return sum_digits


cube_numbers = []
for number in range(1, 1001, 2):
    cube_numbers.append(number ** 3)

sum_numbers = 0
for x in cube_numbers:
    if sum_of_digits(x) % 7 == 0:
        sum_numbers += x
print(sum_numbers)
