def task1(a, b):    
    print(f"S=a*b={a*b}")
    print(f"P=2*(a+b)={2*(a+b)}")

def task2(d):
    print(f"L=pi*d={3.14*d}")
    
def task3(a, b):
    print(f"(a+b)/2={(a+b)/2}")
    
def task4(a, b):
    a2 = a*a
    b2 = b*b
    print(f"a^2+b^2={a2+b2}")
    print(f"a^2-b^2={a2-b2}")
    print(f"a^2*b^2={a2*b2}")
    print(f"a^2/b^2={a2/b2}")
    
def task5(a, b):
    a2 = abs(a)
    b2 = abs(b)
    print(f"|a|+|b|={a2+b2}")
    print(f"|a|-|b|={a2-b2}")
    print(f"|a|*|b|={a2*b2}")
    print(f"|a|/|b|={a2/b2}")

def printTask(n):
    print(f"Task {n}:")
    

printTask(1)
task1(2, 5)
printTask(2)
task2(10)
printTask(3)
task3(4, 6)
printTask(4)
task4(2, 3)
printTask(5)
task5(-5, 5)