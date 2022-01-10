def task1(N):    
    print(f"{N%60}")

def task2(K):
    print(f"{K%7}")
    
def task3(K, N):
    print(f"{(((K-1)+(N-1))%7) + 1}")
    
def task4(A, B, C):
    k = (A//C)*(B//C)
    s = A*B - k*(C*C)
    print(f"{k} - {s}")
    
def task5(x):
    print(f"{x//100 + 1}")

def printTask(n):
    print(f"Task {n}:")
    
printTask(1)
task1(60*100+3)
printTask(2)
task2(8)
printTask(3)
task3(8,2)
printTask(4)
task4(10,10,2)
printTask(5)
task5(2022)