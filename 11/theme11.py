def task1(a,b):    
    if a==b:
        a = b = 0
    else:
        a = b = max(a,b)
    print(f"{a} {b}")

def task2(a, b, c):
    print(f"{a+b+c - min(a,min(b,c))}")
    
def task3(a, b, c):
    l1 = abs(a-b)
    l2 = abs(a-c)
    if l1<l2:
        print(f"b - {l1}")
    else:
        print(f"c - {l2}")
    
def task4(x,y):
    if x>0:
        if y>0:
            print("1")
        else:
            print("4")
    else:
        if y>0:
            print("2")
        else:
            print("3")
    
def task5(a):
    s = ""
    if a == 0:
        s += "нулевое "
    else:
        if a>0:
            s += "положительное "
        else:
            s += "отрицательное "
        if a%2==0:
            s += "четное "
        else:
            s += "нечетное "
    s += "число"
    print(s)

def task6(a):
    s = ""
    if a%2==0:
        s += "четное "
    else:
        s += "нечетное "
    if a<=9:
        s += "однозначное "
    elif a<=99:
        s += "двузначное "
    elif a<=999:
        s += "трехзначное "
    s += "число"
    print(s)

def printTask(n):
    print(f"Task {n}:")
    
printTask(1)
task1(2,5)
printTask(2)
task2(5, 2, 7)
printTask(3)
task3(0, 2, 1)
printTask(4)
task4(10,5)
printTask(5)
task5(-20)
printTask(6)
task6(120)