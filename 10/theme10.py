def task1(a, b):    
    print(f"{(a>2) and (b<=3)}")

def task2(a, b, c):
    print(f"{a<b<c}")
    
def task3(x):
    print(f"{x%2==0 and x>=10 and x<=99}")
    
def task4(x):
    a = x//100
    b = (x%100)//10
    c = x%10
    print(f"{a>b>c or a<b<c}")
    
def task5(x):
    print(f"{x//1000 == x%10 and (x%1000)//100 == (x%100)//10}")
    
def task6(a,b,c):
    t1 = a*a + b*b == c*c
    t2 = a*a + c*c == b*b
    t3 = b*b + c*c == a*a
    print(f"{t1 or t2 or t3}")

def task7(a,b,c):
    t1 = a+b > c
    t2 = a+c > b
    t3 = b+c > a
    print(f"{t1 and t2 and t3}")

def printTask(n):
    print(f"Task {n}:")
    
printTask(1)
task1(5,5)
printTask(2)
task2(5, 6, 7)
printTask(3)
task3(22)
printTask(4)
task4(321)
printTask(5)
task5(2442)
printTask(6)
task6(5,3,4)
printTask(7)
task7(5,3,4)