#!/usr/bin/env python3
import sys, math
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def yes(): print("Yes")
def no(): print("No")
MOD = 1000000007

n,m = LI()
x = 0
for i in range(n):
    A = LI()
    if i == 0:
        if (A[0]-1)%7 + m > 7:
            no()
            break
        x = A[0]
    
    if A[0] != x:
        no()
        break
    for j in range(m-1):
        if A[j]+1 != A[j+1]:
            no()
            exit()
    x += 7
else:
    print("Yes")

