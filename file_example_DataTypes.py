import math


"""вычислить площадь треугольника зная длины его сторон"""
a = 15
b = 11
c = 9

p = (a+b+c)/2

s = math.sqrt(p*(p-a)*(p-b)*(p-c))
print(s)