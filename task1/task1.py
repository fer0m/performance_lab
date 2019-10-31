import os
import sys
import numpy as np

# Убедимся, что нам передают верно количество агрументов.
if len(sys.argv) == 2:
    fn = sys.argv[1]
    if os.path.exists(fn):
        # Откроем файл
        with open(fn) as f:
            # Создадим список и наполним его значениями из файла
            a = []
            for line in f:
                a.append(int(line))

        # Вывод результатов на консоль
        print("%.2f" % float(np.percentile(a, 90)))  # 90 Перцентиль
        print("%.2f" % float(np.median(a)))  # Медиана
        print("%.2f" % float(max(a)))  # Максимальное значение
        print("%.2f" % float(min(a)))  # Минимальное значение
        print("%.2f" % float(sum(a) / len(a)))  # Среднее значение
    else:
        print("ERROR : Файл не найден. Уточните путь\Название файла.")
else:
    print("ERROR : Формат запуска скрипта подразумевает вид 'python task1.py file:/.../text.txt'")
