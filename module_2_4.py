numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
num = 0
for num in numbers:
    if num <= 1:                                # исключение 1 из списка
        continue

    is_prime = True                             # установка флага
    for i in range(2, int(num ** 0.5) + 1):     # цикл подбора делителей для числа num
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(num)
    else:
        not_primes.append(num)

print(primes, not_primes, sep='\n')
