calls = 0  # Глобальная переменная для подсчета вызовов

def count_calls():
    global calls  # Объявление глобальной переменной
    calls += 1  # Увеличиваем счетчик

def string_info(string):
    count_calls()  # Увеличиваем счетчик вызова функции
    return len(string), string.upper(), string.lower()  # Возвращаем кортеж с информации о строке

def is_contains(string, list_to_search):
    count_calls()  # Увеличиваем счетчик вызова функции
    # Приводим строку и все строки в списке к нижнему регистру для сравнения
    return string.lower() in (item.lower() for item in list_to_search)

# Примеры вызовов функций
print(string_info('Capybara'))  # Пример вызова string_info
print(string_info('Armageddon'))  # Пример вызова string_info
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Пример вызова is_contains
print(is_contains('cycle', ['recycling', 'cyclic']))  # Пример вызова is_contains

# Выводим общее количество вызовов
print(calls)  # Вывод количества вызовов
