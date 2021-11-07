from functools import reduce
def task1(A):    
    for i in range(len(A)):
        mxi = A[i].index(max(A[i]))
        mni = A[i].index(min(A[i]))
        t = A[i][mni]
        A[i][mni] = A[i][mxi]
        A[i][mxi] = t
    print(A)

def task2(A, K):
    a = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
    mn = min(map(min, a))
    mx = max(map(max, a))
    mni = 0
    mnx = 0
    for i in range(len(a)):
        if mn in a[i]:
            mni = i
        if mx in a[i]:
            mnx = i
    t = a[mni]
    a[mni] = a[mnx]
    a[mnx] = t
    a = [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]
    print(a)
    
def task3(A):
    pass
    
def task4(A):
    print(sorted(A,key=lambda x: x[0]))
    
def task5(A):
    a = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
    for i in range(len(a)):
        f = True
        for j in range(len(a[i])):
            if a[i][j] % 2 == 0:
                f = False
                break
        if f:
            print(i)
            return
    print(0)

def printTask(n):
    print(f"Task {n}:")
    
A = [[7,2,3],
     [4,5,6],
     [1,8,9]]
printTask(1)
#task1(A)
printTask(2)
#task2(A,1)
printTask(3)
task3(A)
printTask(4)
task4(A)
printTask(5)
task5(A)