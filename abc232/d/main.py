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

h,w = LI()
C = [S() for _ in range(h)]
dp = [[0]*100 for _ in range(100)]
dp[0][0] = 1

ans = 0
for i in range(h):
    for j in range(w):
        if j > 0 and C[i][j] == '.' and dp[i][j-1]:
            dp[i][j] = 1
        if i > 0 and C[i][j] == '.' and dp[i-1][j]:
            dp[i][j] = 1
        if dp[i][j]:
            ans = max(ans, i+j+1)
print(ans)