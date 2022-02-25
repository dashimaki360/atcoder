#!/usr/bin/env python3
import sys, math
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def yes(): print("Yes")
def no(): print("No")
MOD = 1000000007

def janken(x,y):
    if x == y:
        return [0,0]
    elif x=='G' and y=='C':
        return [1,0]
    elif x=='G' and y=='P':
        return [0,1]
    elif x=='C' and y=='P':
        return [1,0]
    elif x=='C' and y=='G':
        return [0,1]
    elif x=='P' and y=='G':
        return [1,0]
    elif x=='P' and y=='C':
        return [0,1]

n,m = LI()
A = [input() for _ in range(2*n)]
L = []
for i in range(2*n):
    L.append([i,0])
for i in range(m):
    for j in range(n):
        a, b = janken(A[L[2*j][0]][i], A[L[2*j+1][0]][i])
        L[2*j][1] += a
        L[2*j+1][1] += b
    L.sort(key=lambda x: (-x[1], x[0]))
for i in range(2*n):
    print(L[i][0]+1)

