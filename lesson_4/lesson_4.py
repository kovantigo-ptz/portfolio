'''
 Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
 и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests.
 В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
 Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
 Можно ли, используя только методы класса str, решить поставленную задачу?
 Функция должна возвращать результат числового типа, например float.
 Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
'''

from sys import argv
from requests import get
from xmltodict import parse
from bs4 import BeautifulSoup
from re import search
from decimal import Decimal
from datetime import datetime

#  ----------Вариант 1----------


def currency_rates(curr_code):
    #  request with return of result in bytes
    response = get('http://www.cbr.ru/scripts/XML_daily.asp').content
    #  converting request content to a dict
    xml_dict = parse(response)
    #  getting a date from the dict and converting to the datetime type
    print(datetime.strptime(xml_dict['ValCurs']['@Date'], '%d.%m.%Y').date(), end=' ')

    for curr_dict in xml_dict['ValCurs']['Valute']:
        if curr_dict['CharCode'] == curr_code:
            #  getting the currency exchange rate and rounding
            print(code, Decimal(curr_dict['Value'].replace(',', '.')).quantize(Decimal("1.00")))
    return 0


#  ----------Вариант 2----------

'''
def currency_rates(curr_code):
    #  request with return of result in text
    response = get('http://www.cbr.ru/scripts/XML_daily.asp').text
    currency_list = response.split('<Valute ')
    #  getting a date from the list and converting to the datetime type
    print(datetime.strptime(search(r'(\d{2}\.){2}\d{4}', currency_list[0])[0], '%d.%m.%Y').date(), end=' ')

    for curr_val in currency_list[1:]:
        #  searching and checking the currency code
        if search(r'[A-Z]{3}', curr_val)[0] == curr_code:
            #  getting the currency exchange rate and rounding
            print(curr_code, Decimal(search(r'[0-9]+.[0-9]{4}',
                                            curr_val)[0].replace(',', '.')).quantize(Decimal("1.00")))
    return 0
'''


#  ----------Вариант 3----------

'''
def currency_rates(curr_code):
    #  request with return of result in text
    response = get('http://www.cbr.ru/scripts/XML_daily.asp').text
    #  creating a BeautifulSoup object. The data is passed to the constructor
    soup = BeautifulSoup(response, 'xml')
    #  date search in the list formed by the find_all method and converting to the datetime type
    print(datetime.strptime(*(val['Date'] for val in soup.find_all('ValCurs')), '%d.%m.%Y').date(), end=' ')
    # creating current codes list
    curr_codes_list = [code.text for code in soup.find_all('CharCode')]
    #  creating current rates list
    curr_rates_list = [rate.text.replace(',', '.') for rate in soup.find_all('Value')]
    #  creating current rates dict, where {curr_code: curr_rate}
    curr_rates_dict = dict(zip(curr_codes_list, curr_rates_list))
    print(curr_code, Decimal(curr_rates_dict[curr_code]).quantize(Decimal("1.00")))
'''

if __name__ == '__main__':
    program_name, code = argv
    exit(currency_rates(code.upper()))
