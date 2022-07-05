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

n,q = LI()
A = LI()
A = deque(A)

for _ in range(q):
    t,x,y = LI()
    x -= 1; y -= 1
    if t == 1:
        A[x], A[y] = A[y], A[x]
    elif t == 2:
        tmp = A.pop()
        A.appendleft(tmp)
    else:
        print(A[x])

