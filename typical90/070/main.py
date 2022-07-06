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

n = I()
X = []
Y = []
for _ in range(n):
    x,y = LI()
    X.append(x)
    Y.append(y)
X.sort()
Y.sort()
gx = X[n//2]
gy = Y[n//2]
ans = 0
for x,y in zip(X,Y):
    ans += abs(gx-x)
    ans += abs(gy-y)
print(ans)



