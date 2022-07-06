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
MOD = 1000000007
INF = 10**18

l,r = LI()

ans = 0
for i in range(1,20):
    low = pow(10,i-1)
    low = max(l,low)
    high = pow(10,i) - 1
    high = min(r,high)
    if low > high: continue
    tmp = (low+high)*(high-low+1)//2
    tmp %= MOD
    tmp *= i
    tmp %= MOD
    ans += tmp
    ans %= MOD
print(ans)