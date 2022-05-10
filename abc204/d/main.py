#!/usr/bin/env python3
import sys, math
sys.setrecursionlimit(10**6)
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def yes(): print("Yes")
def no(): print("No")

n = I()
T = LI()

tot = sum(T)
T.sort()

dp = [[False]*(tot+1) for _ in range(n+1)]
dp[0][0] = True

for i in range(n):
    for j in range(tot+1):
        if dp[i][j]:
            dp[i+1][j] = True
        if j - T[i] >= 0 and dp[i][j-T[i]]:
            dp[i+1][j] = True

ans = float("inf")
for i,t in enumerate(dp[n]):
    if t:
        ans = min(ans, max(i, tot-i))
print(ans)