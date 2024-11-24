def find_password(n):
    digits = list(range(1, n))
    result = ''  # Переменная для пароля
    for i in range(len(digits)):
        # Внутренний цикл по второй цифре пары
        for j in range(i + 1, len(digits)):  # Начинаем с i + 1, чтобы пары были уникальными
            pair_sum = digits[i] + digits[j]
            if n % pair_sum == 0:  # Проверяем кратность
                result += str(digits[i]) + str(digits[j])

    return result


n = int(input('Введите число от 3 до 20: '))
if 3 <= n <= 20:
    result = find_password(n)
    print(f"Нужный пароль для {n}: {result}")
else:
    print("Число должно быть в диапазоне от 3 до 20!")
