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
MOD = 1000000007
INF = 10**18


n = I()
A = LI()
tb = [[] for _ in range(n+1)]
for i, a in enumerate(A):
    tb[a].append(i+1)

# print(tb)
def solve(l,r,x):
    ll = bisect.bisect_left(tb[x], l)
    rr = bisect.bisect_right(tb[x], r)
    ans = rr - ll
    print(ans)

q = I()
for i in range(q):
    l,r,x = LI()
    solve(l,r,x)
