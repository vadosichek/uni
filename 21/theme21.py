from functools import reduce
def task1(A):    
    R = len(A)
    C = len(A[0])
    s = [[0 for i in range(C)] for j in range(R)]    
    d = [[1, 0, -1, 0],
         [0, 1, 0, -1]]
    p = [0,0]
    di = 0
 
    for i in range(R * C):
        print(A[p[0]][p[1]], end=' ')
        s[p[0]][p[1]] = True
        
        cp = [p[0] + d[0][di],
              p[1] + d[1][di]]
 
        if (0 <= cp[0] and cp[0] < R) and (0 <= cp[1] and cp[1] < C) and not s[cp[0]][cp[1]]:
                p = cp
        else:
            di = (di + 1) % 4
            p = [p[0] + d[0][di],
                 p[1] + d[1][di]]
    print()

def task2(A, K):
    s = reduce(lambda r, x: r + x, A[K], 0)
    p = reduce(lambda r, x: r * x, A[K], 1)
    print(s, p)
    
def task3(A):
    a = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
    p = [[i,reduce(lambda r, x: r * x, a[i], 1)] for i in range(len(a))]
    p = sorted(p, key=lambda x: x[1])
    print(p[0])
    
def task4(A):
    a = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
    sr = [reduce(lambda r, x: r + x, a[i], 0)/len(a[i]) for i in range(len(a))]
    c = [len([x for x in a[i] if x > sr[i]]) for i in range(len(a))]
    print(c)
    
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
    
A = [[1,2,3],
     [4,5,6],
     [7,8,9]]
printTask(1)
task1(A)
printTask(2)
task2(A,1)
printTask(3)
task3(A)
printTask(4)
task4(A)
printTask(5)
task5(A)