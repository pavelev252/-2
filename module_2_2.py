try:
    first, second, third = map(int, input("Введите три числа через пробел: ").split())
    if first == second == third:
        print(3)
    elif len({first, second, third}) < 3:
        print(2)
    elif len({first, second, third}) == 3:
        print(0)
except ValueError:
    print("Не коректный ввод, попробуйте еще раз")
