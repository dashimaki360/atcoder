#!/usr/bin/env python3
import sys, math ,heapq, bisect
from collections import deque
sys.setrecursionlimit(10**6)
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def yes(): print("Yes")
def no(): print("No")
MOD = 1000000007
INF = 10**18

n,l,r = LI()
A = LI()
sumA = [0]*(n+1)
C = [0]*(n+1)
minC = [0]*(n+1)
for i in range(n):
    sumA[i+1] = sumA[i] + A[i]
    C[i+1] = C[i] + (l - A[i])
    if minC[i] >= C[i+1]:
        minC[i+1] = C[i+1]
    else:
        minC[i+1] = minC[i]

ans = INF
for i in range(n+1):
    tmp = r*(n-i)
    tmp += minC[i]
    tmp += sumA[i]
    ans = min(ans, tmp)
print(ans)
    


