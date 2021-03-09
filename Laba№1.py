import time
import random
import math


def eratosthenes(n):     # n - число, до которого хотим найти простые числа 
    sieve = list(range(n + 1))
    sieve[1] = 0    # без этой строки итоговый список будет содержать единицу
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    return set(x for x in sieve if x != 0)

#Возвращает множители числа n
def factor(n):
    factors = set()
    d = 2
    while d*d <= n:
        if n % d == 0:
            factors.add(d)
            n //= d
        else:
            d +=1
    if n > 1:
        factors.add(n)
    return factors


def is_awful_naive(number):
    #Функция проверки числа на простоту
    def IsPrime(n):
        d = 2
        while d <= n and n % d != 0:
            d += 1
        return d * d > n
    
    factors = factor(n)
    for x in factors:
        if not IsPrime(x):
            return False
    return True


def is_awful_optimized(n):
    factors = factor(n)
    #Простые числа от 2 до sqrt(n)
    PrimeNumbers = eratosthenes(int(math.sqrt(n)+1))
    #Составные числа от 2 до sqrt(n)
    NotPrimeNumbers = set(range(2, int(math.sqrt(n)) +2)) - PrimeNumbers
    #Пересечение множеств множителей n и составных чисел
    #Если среди множителей числа n нет простых чисел, то вернется пустое множество
    return  not bool(factors & NotPrimeNumbers)

error = 0
for _ in range(1000):
    n = random.randint(100, 1000000)
    start_time = time.time()
    is_awful_naive(n)
    time1 =time.time() - start_time
    start_time = time.time()
    is_awful_optimized(n)
    time2 = time.time() - start_time
    error += time1 - time2
    #print(f'n={n}  {round(time1*1000, 4)}  {round(time2*1000, 4)}')
print(error/1000)



