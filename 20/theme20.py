from math import sqrt, pow

def genSeries(A):
    s = []
    p = 0
    for i in range(1, len(A)):
        if A[i] != A[i-1]:
            s.append([p,i-p,A[i-1]])
            p = i
    s.append([p,len(A)-p,A[i-1]])
    return s

def genFromSeries(s):
    s = sorted(s, key=lambda x: x[0])
    A = []
    for i in s:
        for j in range(i[1]):
            A.append(i[2])
    return A
        

def task1(A):
    s = genSeries(A)
    B = [x[1] for x in s]
    C = [x[2] for x in s]
    print(B)
    print(C)
    
def task2(A, L):
    s = genSeries(A)
    for i in range(len(s)):
        if s[i][1] > L:
            s[i][1] = 1
            s[i][2] = 0
    print(genFromSeries(s))
    
def task3(A, K):
    s = genSeries(A)
    a1 = genFromSeries(s[:K:])
    k = genFromSeries([s[K]])
    a2 = genFromSeries(s[K+1:len(s)-1])
    l = genFromSeries([s[-1]])
    print([*a1,*l,*a2,*k])
    
def dist(x):
    return sqrt(pow(x[0],2)+pow(x[1],2))

def dist2(x,y):
    return sqrt(pow(x[0]-y[0],2)+pow(x[1]-y[1],2))

def task4(A):
    a = [x for x in A if (x[0]<=0 and x[1]>=0)]
    if len(a) == 0:
        print([0,0])
        return
    a = sorted(a, key=dist)
    print(a[-1])
    
    
def per(a,b,c):
    return dist2(a,b) + dist2(b,c) + dist2(c,a)

def task5(A):
    p = 0
    s = None
    for a in range(len(A)):
        for b in range(len(A)):
            if b != a:
                for c in range(len(A)):
                    if c!=a and c!=b:
                        if per(A[a], A[b], A[c]) > p:
                            p = per(A[a], A[b], A[c])
                            s = [A[a], A[b], A[c]]
    print(p,s)

def printTask(n):
    print(f"Task {n}:")

A = [1,2,2,3,3,3,1,4,4,4,4]
B = [[0,1],[1,0],[0,-1],[-1,0],[1,1],[-1,-1],[-1,1],[1,-1]]
printTask(1)
task1(A)
printTask(2)
task2(A,2)
printTask(3)
task3(A,1)
printTask(4)
task4(B)
printTask(5)
task5(B)
