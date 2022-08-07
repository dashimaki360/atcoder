#!/usr/bin/env python3
import sys, math ,heapq, bisect
from collections import deque
sys.setrecursionlimit(10**6)
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def yes(): print("Yes")
def no(): print("No")
MOD = 1000000007
INF = 10**18

n = int(input())
m = 1 << n
c = [[0] + list(map(int, input().split())) for _ in range(m)]

# 1試合毎の獲得金に修正する
for i in range(m):
    for j in range(n):
        c[i][j] = c[i][j + 1] - c[i][j]

dp = [[0] * m for _ in range(n+1)]

for i in range(n):
    d = 1 << (i)
    for j in range(0, m, d * 2):
        m1 = max(dp[i][j:j+d])
        m2 = max(dp[i][j+d:j+d+d])
        for k in range(j, j + d):
            dp[i + 1][k] = dp[i][k] + m2 + c[k][i]
        for k in range(j+d, j+d + d):
            dp[i + 1][k] =  dp[i][k] + m1 + c[k][i]
print(max(dp[n]))
