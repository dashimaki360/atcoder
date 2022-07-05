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

k = I()

if k%9:
    print(0)
    exit()

dp = [0]*(k+100)
dp[0] = 1
ans = 0
for i in range(k):
    for j in range(1,10):
        dp[i+j] += dp[i]
        dp[i+j] %= MOD
ans = dp[k]%MOD
print(ans)
