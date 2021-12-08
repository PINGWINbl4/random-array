import random
from loguru import logger
logger.add("log.log", format="{time} {level} {message}", level="DEBUG")
print('Введите целое число - количество эллементов')
try:
    while True:
        n = int(input())
        break
except(Exception):
    logger.info(n)
    logger.error('')
    print('Вы ввели некорректоное число')
a = []
for i in range(n):
    a.append(i+1)

while a !=[]:
    x = random.randint(0, n-1)
    print(a[x], end=' ')
    n -= 1
    a.pop(x)
print()
logger.info(n)
