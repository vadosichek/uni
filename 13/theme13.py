def task1(x):    
    for i in range(1,11):
        print(f"{i/10} - {i/10*x}")

def task2(n):
    r = 1
    for i in range(1,n+1):
        r*=(1+0.1*i)
    print(r)
    
def task3(n):
    r = 0
    for i in range(1, n+1):
        r += (2*i-1)
        print(r)
    print(r)
    
def task4(a, n):
    r = 1
    p = 1
    for i in range(1,n+1):
        p*=a
        r+=p
    print(r)
    
def task5(a, n):
    r = 1
    p = 1
    for i in range(1,n+1):
        p*=a*(-1)
        r+=p
    print(r)

def printTask(n):
    print(f"Task {n}:")
    
printTask(1)
task1(10)
printTask(2)
task2(3)
printTask(3)
task3(6)
printTask(4)
task4(2,2)
printTask(5)
task5(2,2)