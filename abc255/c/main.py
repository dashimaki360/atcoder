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

if d < 0:
    # a = a + d*(n-1)
    # d = -d
    a = -a
    d = -d
    x = -x

if x > a+d*(n-1):
    ans = x-(a+d*(n-1))
    print(ans)
elif a >= x:
    ans = a-x
    print(ans)
else:
    ans = min((x-a)%d, d-((x-a)%d))
    print(ans)

