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

h,w = LI()
B = [S() for _ in range(h)]
A = [[0]*(w) for _ in range(h)]
for i in range(h):
    for j in range(w):
        if B[i][j] == "+":
            A[i][j] = 1
        else:
            A[i][j] = -1

dp = [[0]*(w) for _ in range(h)]
for i in reversed(range(h)):
    for j in reversed(range(w)):
        if i == h-1 and j == w-1: continue
        if (i+j)%2 == 0: #Takahashi
            dp[i][j] = -INF
            if i+1 < h:
                dp[i][j] = max(dp[i][j], dp[i+1][j] + A[i+1][j])
            if j+1 < w:
                dp[i][j] = max(dp[i][j], dp[i][j+1] + A[i][j+1])
        else: #Aoki
            dp[i][j] = INF
            if i+1 < h:
                dp[i][j] = min(dp[i][j], dp[i+1][j] - A[i+1][j])
            if j+1 < w:
                dp[i][j] = min(dp[i][j], dp[i][j+1] - A[i][j+1])
ans = "Draw"
if dp[0][0] > 0:
    ans = "Takahashi"
elif dp[0][0] < 0:
    ans = "Aoki"
print(ans)
