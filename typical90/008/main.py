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
s = input()
atc = "atcoder"
dp = [0]*(1 + len(atc))
dp[0] = 1

for i in range(n):
    tmp = dp.copy()
    for j,c in enumerate(atc):
        if s[i] == c:
            dp[j+1] += tmp[j]
            dp[j+1] %= MOD
ans = dp[-1]
print(ans%MOD)
