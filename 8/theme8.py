from math import radians, degrees

def task1(a):    
    print(f"{a//1024}")

def task2(a, b):
    print(f"{a//b}")
    
def task3(a, b):
    print(f"{a-(a//b)*b}")
    
def task4(a):
    a = (a%10)*10 + a//10
    print(f"{a}")
    
def task5(a):
    a = (a%100)*10 + a//100
    print(f"{a}")

def printTask(n):
    print(f"Task {n}:")
    
printTask(1)
task1(1025)
printTask(2)
task2(5, 2)
printTask(3)
task3(5, 2)
printTask(4)
task4(25)
printTask(5)
task5(123)