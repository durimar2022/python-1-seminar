# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

c = int(input ("Введите четверть "))
if c == 1:
    print("x>0 and y>0")
elif c == 2:
    print("x<0 and y>0")
elif c == 3:
    print("x<0 and y<0")
elif c == 4:
    print("x>0 and y<0")
else:
     print ("введите четверть от 1 до 4")