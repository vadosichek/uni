def task1(a,b):   
    for i in range (a,b+1):
        for j in range(i):
            print(i)

def task2(a, b):
    t = a
    while t>=0:
        t-=b
    print(t+b)
    
def task3(n):
    k=0
    t=0
    while t<n:
        k+=1
        t+=k
    print(f"{k} - {t}")
    
def task4(p):
    k=1
    s=1000
    while s<=1100:
        k+=1
        s*=(100+p)/100
    print(f"{k} - {s}")
    
def task5(a, b):
    while not(a==0) and not(b==0):
        if a>b:
            a%=b
        else:
            b%=a
    print(a+b)

def task6(n):
    a1=1
    a2=2
    f=0
    k=2
    while f<n:
        k+=1
        f=a1+a2
        a2=a1
        a1=f
    print(k)

def printTask(n):
    print(f"Task {n}:")
    
printTask(1)
task1(1, 5)
printTask(2)
task2(5, 3)
printTask(3)
task3(5)
printTask(4)
task4(10)
printTask(5)
task5(128, 64)
printTask(6)
task6(55)