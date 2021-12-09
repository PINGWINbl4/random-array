import random
from loguru import logger
# Создаем лог файл
logger.add("log.log", format="{time} {level} {message}", level="DEBUG")
print('Введите целое число - количество эллементов')
try:
    while True:
        n = int(input())
        break
except(Exception):
    logger.info(n)
    logger.error('некорректоное число')
    print('Вы ввели некорректоное число')
# Формируем строку из аллементов
logger.info(n)
a = []
new_a = []
for i in range(n):
    a.append(i+1)
# Пишем случайный элемент(если быть точнее, эллемент со случайным индексом)
while a !=[]:
    x = random.randint(0, n-1)
    print(a[x], end=' ')
    new_a.append(a[x])
# Удаляем выведенный элемент
    n -= 1
    a.pop(x)
print()
logger.info(str(new_a))
