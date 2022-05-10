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
if n == 0:
    print(0)
    exit()

ans = INF
for a in range(10**6):
    ok = 10**6
    ng = 0
    while ok - ng > 1:
        b = (ok+ng)//2
        x = a**3 + a*a*b + a*b*b + b**3
        if x >= n:
            ok = b
        else:
            ng = b
    x = a**3 + a*a*ok + a*ok*ok + ok**3
    ans = min(ans, x)
print(ans)


