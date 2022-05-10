#!/usr/bin/env python3
import sys, math
sys.setrecursionlimit(10**6)
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def yes(): print("Yes")
def no(): print("No")
MOD = 1000000007
INF = 10**18

h, w, c = LI()
A = [LI() for _ in range(h)]
dp = [[INF]*(w) for _ in range(h)]
ans = INF

for i in range(h):
    for j in range(w):
        if i == 0 and j == 0:
            dp[i][j] = A[i][j]
            continue
        if i == 0:
            dp[i][j] = min(A[i][j], dp[i][j-1]+c)
            continue
        if j == 0:
            dp[i][j] = min(A[i][j], dp[i-1][j]+c)
            continue
        dp[i][j] = min(min(A[i][j], dp[i-1][j]+c), dp[i][j-1]+c)
for i in range(h):
    for j in range(w):
        if i != 0:
            ans = min(ans, dp[i-1][j]+A[i][j]+c)
        if j != 0:
            ans = min(ans, dp[i][j-1]+A[i][j]+c)

A.reverse()
for i in range(h):
    for j in range(w):
        if i == 0 and j == 0:
            dp[i][j] = A[i][j]
            continue
        if i == 0:
            dp[i][j] = min(A[i][j], dp[i][j-1]+c)
            continue
        if j == 0:
            dp[i][j] = min(A[i][j], dp[i-1][j]+c)
            continue
        dp[i][j] = min(min(A[i][j], dp[i-1][j]+c), dp[i][j-1]+c)
for i in range(h):
    for j in range(w):
        if i != 0:
            ans = min(ans, dp[i-1][j]+A[i][j]+c)
        if j != 0:
            ans = min(ans, dp[i][j-1]+A[i][j]+c)

print(ans)