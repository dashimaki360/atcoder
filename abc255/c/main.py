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

x,a,d,n = LI()

if d == 0:
    ans = abs(x-a)
    print(ans)
    exit()

x = x-a
if d < 0:
    d = -d
    x = -x

if x > d*(n-1):
    ans = x-d*(n-1)
    print(ans)
elif 0 >= x:
    ans = -x
    print(ans)
else:
    ans = min(x%d, d-(x%d))
    print(ans)

