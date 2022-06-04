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
A = LI()
C = [0]*(2*100000+5)
for a in A:
    C[a] += 1

dp = [1,0,0,0]
for i in range(len(C)):
    tmp = dp.copy()
    dp[0] = tmp[0]
    dp[1] = tmp[1] + tmp[0]*C[i]
    dp[2] = tmp[2] + tmp[1]*C[i]
    dp[3] = tmp[3] + tmp[2]*C[i]

ans = dp[3]
print(ans)


