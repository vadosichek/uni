def task1(a):   
    a = [[x] for x in a]
    for x in a:
        PowerA3(x,x)
    print(f"{[x[0] for x in a]}")

def PowerA3(a,b):
    b[0] = a[0]*a[0]*a[0]

def task2(a, b):
    print(f"{Sign(a) + Sign(b)}")
    
def Sign(x):
    if x<0:
        return -1
    elif x==0:
        return 0
    else:
        return 1
    
def task3(a):
    for i in a:
        print(f"{i} - {RingS(i[0],i[1])}")
    
def RingS(r1, r2):
    return 3.14*(r1*r1 - r2*r2)
    
def task4(x,y):
    print(f"{Quarter(x,y)}")

def Quarter(x,y):
    if x>0:
        if y>0:
            return 1
        else:
            return 4
    else:
        if y>0:
            return 2
        else:
            return 3
    
def task5(a):
    print(f"{[Fact2(x) for x in a]}")
    
def Fact2(n):
    r=1
    while n>0:
        r*=n
        n-=2
    return r

def printTask(n):
    print(f"Task {n}:")
    
printTask(1)
task1([1,2,3,4,5])
printTask(2)
task2(1.1, -1.2)
printTask(3)
task3([[2,1],[3,2],[4,3]])
printTask(4)
task4(10,5)
printTask(5)
task5([1,2,3,4,5])