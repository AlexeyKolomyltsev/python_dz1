# Напишите программу, которая принимает на вход координаты точки (X и Y),
#  причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
#  в которой находится эта точка (или на какой оси она находится).
x = int(input("Введите координаты X "))
y = int(input("Введите координаты Y "))
if x > 0 and y > 0:
    print(f"({x},{y}) - 1 четверть")
elif x < 0 and y > 0:
    print(f"({x},{y}) - 2 четверть")
elif x < 0 and y < 0:
    print(f"({x},{y}) - 3 четверть")
elif x > 0 and y < 0:
    print(f"({x},{y}) - 4 четверть")    