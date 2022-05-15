#!/usr/bin/env python3
import sys, math ,heapq, bisect
from collections import deque
sys.setrecursionlimit(10**6)
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def yes(): print("Yes")
def no(): print("No")
MOD = 998244353
INF = 10**18

n,w = LI()
A = LI()
flag = [0]*(w+10)
for i in range(n):
    tmp = A[i]
    if tmp <= w:
        flag[tmp] = 1

for i in range(n):
    for j in range(i+1,n):
        tmp = A[i] + A[j]
        if tmp <= w:
            flag[tmp] = 1

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            tmp = A[i] + A[j] +A[k]
            if tmp <= w:
                flag[tmp] = 1
ans = sum(flag)
print(ans)


