#1
def lenght(x1, y1, x2, y2):
    s = ((x2-x1)**2+(y2-y1)**2)**(1/2)
    return s

x1 = int(input("x1="))
y1 = int(input("y1="))
x2 = int(input("x2="))
y2 = int(input("y2="))
x3 = int(input("x3="))
y3 = int(input("y3="))
print(f"1 сторона  {lenght(x1, y1, x2, y2)}")
print(f"2 сторона  {lenght(x3, y3, x1, y1)}")
print(f"3 сторона  {lenght(x2, y2, x3, y3)}")

#2
def check(a, b, c):
    if a+b>c and b+c>a and c+a>b:
        return True
    else:
        return False
a = int(input("A="))
b = int(input("B="))
c = int(input("C="))
if check(a, b, c):
    print("Треугольник существует")
else:
    print("Треугольник не существует")

#3
import math
def area(a, b, c):
    p=(a+b+c)/2
    s=math.sqrt(p*(p-a)*(p-b)*(p-c))
    return s
def check(a, b, c):
    if a+b>c and b+c>a and c+a>b:
        return True
    else:
        return False
a = int(input("A="))
b = int(input("B="))
c = int(input("C="))
if check(a, b, c):
    print(f"Площадь треугольника {area(a, b, c)}")
else:
    print("Треугольник не существует")

#4
import math
def lenght(x1, y1, x2, y2):
    s = ((x2-x1)**2+(y2-y1)**2)**(1/2)
    return s
def area(a, b, c):
    p=(a+b+c)/2
    s=math.sqrt(p*(p-a)*(p-b)*(p-c))
    return s
def check(a, b, c):
    if a+b>c and b+c>a and c+a>b:
        return True
    else:
        return False
x1 = int(input("x1="))
y1 = int(input("y1="))
x2 = int(input("x2="))
y2 = int(input("y2="))
x3 = int(input("x3="))
y3 = int(input("y3="))
a = lenght(x1, y1, x2, y2)
b = lenght(x3, y3, x1, y1)
c = lenght(x2, y2, x3, y3)
if check(a, b, c):
    print(f"Площадь треугольника {area(a, b, c)}")
else:
    print("Треугольник не существует")

#5
t = [0 for i in range(19)]
for i in range(99): t[i // 10 + i % 10] += 1
print(f"Количество призов {sum([i * i for i in t])} штук")