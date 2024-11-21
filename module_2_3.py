my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
n = 0
element = -1
while n != len(my_list):
    element += 1
    if element >= len(my_list):
        break
    if my_list[element] > 0:
        n += 1
        print(my_list[element])
    elif my_list[element] < 0:
        break
