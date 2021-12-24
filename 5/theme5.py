from math import sqrt, pow

def task1(x1, y1, x2, y2):    
    d = sqrt(pow(x1-x2,2)+pow(y1-y2,2))
    print(f"d={d}")

def task2(A, B, C):
    ac = abs(A-C)
    bc = abs(B-C)
    print(f"ac={ac}")
    print(f"bc={bc}")
    print(f"sum={ac+bc}")
    
def task3(A, B, C):
    print(f"|AC|*|BC|={abs(C-A)*abs(B-C)}")
    
def task4(x1, y1, x2, y2):
    a = abs(x1-x2)
    b = abs(y1-y2)
    print(f"P={2*(a+b)}")
    print(f"S={a*b}")
    
def task5(x1, y1, x2, y2, x3, y3):
    a = sqrt(pow(x1-x2,2)+pow(y1-y2,2))
    b = sqrt(pow(x2-x3,2)+pow(y2-y3,2))
    c = sqrt(pow(x1-x3,2)+pow(y1-y3,2))
    P = a+b+c
    p = P/2
    s = sqrt(p*(p-a)*(p-b)*(p-c))
    print(f"P={P}")
    print(f"S={s}")
    

def printTask(n):
    print(f"Task {n}:")
    
printTask(1)
task1(2, 5, 2, 6)
printTask(2)
task2(2,5,10)
printTask(3)
task3(4, 10, 6)
printTask(4)
task4(0,0,2,5)
printTask(5)
task5(0, 0, 2, 5, -4, 3)