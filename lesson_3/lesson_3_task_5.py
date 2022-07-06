'''
5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
взятых из трёх списков (по одному из каждого):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
Например:
>>> get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]
Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг,
разрешающий или запрещающий повторы слов в шутках (когда каждое слово можно использовать только в одной шутке)?
'''
from random import shuffle, sample, choice


def get_jokes(count_jokes, flag=False):
    '''
    Generate jokes

    :param count_jokes: count of jokes generated
    :param flag: flag is True, when you need to generate jokes without repeating words
    :return: list of jokes
    '''
    joke_list = []
    if flag:
        shuffle(nouns)
        shuffle(adverbs)
        shuffle(adjectives)
        #  combining words into tuples
        for noun, adverb, adjective in zip(sample(nouns, count_jokes), adverbs, adjectives):
            joke_list.append(f'{noun} {adverb} {adjective}')
    else:
        for index in range(count_jokes):
            joke_list.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
    return joke_list


nouns = ['автомобиль', 'лес', 'огонь', 'город', 'дом', 'школа', 'лодка']
adverbs = ['сегодня', 'вчера', 'завтра', 'позавчера', 'ночью', 'утром']
adjectives = ['веселый', 'яркий', 'зеленый', 'утопичный', 'мягкий']
print(get_jokes(4, flag=True))
