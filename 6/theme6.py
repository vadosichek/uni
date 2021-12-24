from math import sqrt, pow

def task1(a, b):    
    t = a
    a = b
    b = t
    print(f"a={a}")
    print(f"b={b}")

def task2(a, b, c):
    t = b
    b = a
    a = c
    c = t
    print(f"a={a}")
    print(f"b={b}")
    print(f"c={c}")
    
def task3(a, b, c):
    t = c
    c = a
    a = b
    b = t
    print(f"a={a}")
    print(f"b={b}")
    print(f"c={c}")
    
def task4(x):
    y = 3*pow(x,6)-6*pow(x,2)-7
    print(f"y(x)={y}")
    
def task5(x):
    y = 4*pow(x-3,6)-7*pow(x-3,3)+2
    print(f"y(x)={y}")

def task6(a):
    b = a*a
    b = b*b
    b = b*b
    print(f"A^8={b}")

def task7(a):
    b = a*a
    c = a*b*b
    b = c*c*c
    print(f"A^15={b}")

def printTask(n):
    print(f"Task {n}:")
    
printTask(1)
task1(1, 2)
printTask(2)
task2(1, 2, 3)
printTask(3)
task3(1, 2, 3)
printTask(4)
task4(1)
printTask(5)
task5(4)
printTask(6)
task6(2)
printTask(7)
task7(2)