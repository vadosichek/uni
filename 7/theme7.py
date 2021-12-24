from math import radians, degrees

def task1(a):    
    print(f"a={radians(a)} radians")

def task2(a):
    print(f"a={degrees(a)} degrees")
    
def task3(x, a, y):
    pr = a/x
    print(f"1 (kg) = {pr}")
    print(f"y (kg) = {pr*y}")
    
def task4(v1, v2, s, t):
    print(f"L={s+v1*t+v2*t}")
    
def task5(a, b):
    print(f"x=-b/a={-1*b/a}")

def task6(a1,b1,c1,a2,b2,c2):
    y = (a1*c2-a2*c1)/(a1*b2-a2*b1)
    x = c1/a1 - y*(b1/a1)
    print(f"x={x}")
    print(f"y={y}")

def printTask(n):
    print(f"Task {n}:")
    
printTask(1)
task1(180)
printTask(2)
task2(3.14)
printTask(3)
task3(5, 10, 2)
printTask(4)
task4(1, 2, 4, 5)
printTask(5)
task5(2, 10)
printTask(6)
task6(1,2,3,4,5,6)