#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# X = float (input('Введите X1 '))
# Y = float (input('Введите Y1 '))
# B = float (input('Введите X2 '))
# C = float (input('Введите Y1 '))
#
# s = ((B - X) ** 2 + (C - Y) ** 2) ** 0.5
# print (f"Расстояние между заданными точками равно {int(s * 100) / 100} ")

mas = []
for i in range(4):
    xy = ['x1', 'y1', 'x2', 'y2']
    mas.append(float(input(f'Введите точку {xy[i]} ')))
lenght = float(((mas[2] - mas[0]) ** 2 + (mas[1] - mas[3]) ** 2) ** 0.5)
print(f"Расстояние между заданными точками равно {int(lenght * 100) / 100}")
