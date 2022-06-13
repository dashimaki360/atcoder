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
A.sort()
Asum = [0]*(n+1)
for i, a in enumerate(A):
    Asum[i+1] = Asum[i]+a

for _ in range(q):
    x = I()
    ri = bisect.bisect_right(A,x)
    ans = x*ri - Asum[ri]
    ans += Asum[n] - Asum[ri] - x*(n-ri)
    print(ans)