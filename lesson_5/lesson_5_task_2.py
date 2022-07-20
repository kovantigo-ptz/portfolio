'''
2. * (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.
'''


odd_nums_gen = (num for num in range(1, int(input()) + 1, 2) if num % 2 != 0)
print(*odd_nums_gen)
