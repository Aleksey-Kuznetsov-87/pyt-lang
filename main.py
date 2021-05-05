duration = int(input())    # переменная для ввода данных (в данном случае секунды)
time_m, time_h, time_d = 0, 0, 0    # задаём переменные времени (минуты, часы, дни). и приарвниваем к нулю
if duration < 60:    # если меньше минуты то
    print(duration, ' сек')    # выводим значение секунд
else:    # иначе вычисляем дальше
    time_m = duration//60   # минуты
    if time_m >= 60:
        time_h = time_m//60   # часы
        if time_h >= 24:
            time_d = time_h//24   # сутки
            print(time_d, ' дн', end=' ')
        print(time_h % 24, ' час', end=' ')
    print(time_m % 60, ' мин', end=' ')
    print(duration % 60, ' сек')   # не стал писать отдельное вычисление, оно и в выводе нормально сработает
