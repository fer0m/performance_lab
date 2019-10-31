import os
import sys

'''Данная функция переводит список времени формата hhmm в список времени mm. 
   Проще говоря, переводим все значения в минуты, для удобства работы.'''
def get_time_to_number(new_list):
    list_with_time = []
    for time in new_list:
        first_step = time.strip().split(" ")
        first_time = (first_step[0].split(":"))
        second_time = (first_step[1].split(":"))
        list_with_time.append(
            (int(first_time[0]) * 60 + int(first_time[1]), int(second_time[0]) * 60 + int(second_time[1])))
    return list_with_time


# Проверка на пересечение значений.
def getOverlapping(A_st, A_end, B_st, B_end):
    if A_st == B_st and A_end == B_end:
        pass
    elif A_st < B_end and A_end > B_st:
        if A_st <= B_st:
            C_st = B_st
            if A_end > B_end:
                C_end = B_end
            else:
                C_end = A_end
        else:
            C_st = A_st
            if A_end > B_end:
                C_end = B_end
            else:
                C_end = A_end
        return C_st, C_end
    else:
        pass

# Данная функция создает для нас общий список со всеми пересечениями значений.
def get_list_with_overlapping(time):
    time_range = []
    for mainelem in time:
        for everyelem in time:
            time_range.append(getOverlapping(mainelem[0], mainelem[1], everyelem[0], everyelem[1]))
    time_range = list(set(time_range))
    time_range = [x for x in time_range if x]
    return time_range

# Схлопываем список со всеми значениями до списка пересечения "по границам"
def summ_coordinate(final_time_range):
    b = []
    for begin, end in sorted(final_time_range):
        if b and b[-1][1] >= begin - 1:
            b[-1] = (b[-1][0], end)
        else:
            b.append((begin, end))
    return sorted(b)

# Создаем новый список с финальным пересечением в формате hhmm
def back_to_time(list_with_sum_coordinate):
    list_with_final_time = []
    for elem in list_with_sum_coordinate:
        first_time = str(format_seconds_to_hhmm(elem[0]))
        second_time = str(format_seconds_to_hhmm(elem[1]))
        list_with_final_time.append((first_time, second_time))
    return list_with_final_time

# Перевод минут в формат hhmm
def format_seconds_to_hhmm(minutes):
    hours = minutes // 60
    minutes %= 60
    return "%02i:%02i" % (hours, minutes)


if len(sys.argv) == 2:
    fn = sys.argv[1]
    if os.path.exists(fn):
        # Откроем файл
        with open(fn) as f:
            a = []
            for line in f:
                a.append(line)

        # Получаем список времени переведенного в минуты
        main_list_step_one = get_time_to_number(a)

        # Получаем список с "пересечениями"
        main_list_step_two = get_list_with_overlapping(main_list_step_one)

        # Из списка с "пересечениями" получаем список с объединенными значениями / Обобщаем пересечения
        main_list_step_three = summ_coordinate(main_list_step_two)

        # Переводим в списке минуты во время формата hhmm
        main_list_step_four = back_to_time(main_list_step_three)

        # Выводим результат
        for time in main_list_step_four:
            print(time[0], time[1])

    else:
        print("ERROR : Файл не найден. Уточните путь\Название файла.")
else:
    print("ERROR : Формат запуска скрипта подразумевает вид 'python task1.py file:/.../text.txt'")