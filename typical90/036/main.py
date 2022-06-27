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

n,Q = LI()
X = []
Y = []
for _ in range(n):
    x,y = LI()
    xx = x-y
    yy = x+y
    X.append(xx)
    Y.append(yy)
maxx = max(X)
minx = min(X)
maxy = max(Y)
miny = min(Y)
for _ in range(Q):
    q = I()
    q -= 1
    ans = 0
    ans = max(ans, abs(X[q]-maxx))
    ans = max(ans, abs(X[q]-minx))
    ans = max(ans, abs(Y[q]-maxy))
    ans = max(ans, abs(Y[q]-miny))
    print(ans)


