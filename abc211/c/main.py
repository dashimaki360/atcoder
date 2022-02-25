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

s = S()
t = "chokudai"
dp = [[0 for _ in range(9)] for _ in range(len(s)+1)]
for i in range(len(s)+1):
    dp[i][0] = 1

for i in range(len(s)+1):
    for j in range(9):
        if i == 0: continue
        if j == 0: continue
        if s[i-1] == t[j-1]:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        else:
            dp[i][j] = dp[i-1][j]
ans = dp[len(s)][8] % MOD
print(ans)


