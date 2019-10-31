import glob
import os
import sys


# Функция суммирования пяти списков (Тут "мягко" говоря костыль, но рабочий!)
def sum_my_list(val):
    list_with_sum = list(a + b + c + d + e for a, b, c, d, e in zip(val[0], val[1], val[2], val[3], val[4]))
    return list_with_sum


# Убедимся, что нам передают верно количество агрументов.
if len(sys.argv) == 2:
    fn = sys.argv[1]
    # Создадим "список со списками"
    list_with_filename = []

    # Проверяем, что txt файлов на проверку, согласно заданию - 5.
    if len(glob.glob(os.path.join(fn, '*.txt'))) == 5:
        for filename in glob.glob(os.path.join(fn, '*.txt')):
            with open(filename, 'r') as f:
                filename = []
                # Заполняем список значениями из файла
                for line in f:
                    filename.append(float(line))
                # Добавляем список со значениями, в "список для списков"
                list_with_filename.append(filename)

        variate = sum_my_list(list_with_filename)
        # Получаем максимальный интервал
        print(variate.index(max(variate)) + 1)
    else:
        print("ERROR: Уточните путь к каталогу. Количество txt файлов в каталоге должно быть 5.")
else:
    print("ERROR: Недопустимое количество агрументов! Формат запуска скрипта подразумевает вид 'python task3.py' "
          "file:/.../")
