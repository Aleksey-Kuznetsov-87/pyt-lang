cube_number = []    # задаём пустой список
cube_number_new = []
all_sum = 0    # сумма всех чисел
length_str = 0    # переменная для приравнивания и работы с длиной строки от 1 до 1001 - последнее число не считается
for i in range(1, 1001, 2):    # для каждого i в списке от 1 до 1001
    i = i**3    # возводим i в куб
    cube_number.append(i)    # добавляем значение i в список
for i in cube_number:    # берём каждый элемент списка cube_number
    i = i + 17    # прибавляем к каждому значению i число 17
    cube_number_new.append(i)    # создаём новый список
for j in cube_number_new:    # для каждого значения j
    length_str = len(str(j))   # длина строки
    sum_j = 0    # сумма чисел от j
    x = 0    # задаём считчик (обнуляется при взятии нового числа)
    while x <= length_str:    # пока счётчик меньше длины строки
        sum_j = sum_j + j % 10    # к sum_j добавляем остаток от деления j на 10
        x = x + 1    # добавляем 1 к счётчику
        j = j // 10    # убираем у числа j последнюю цифру
        if sum_j % 7 == 0:    # если sum_j кратно 7, то
            all_sum = + sum_j    # к переменной all_sum прибаляем значение sum_j
print(all_sum)    # выводим суммы чисел
