#!/usr/bin/env python3
import sys, math
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def yes(): print("Yes")
def no(): print("No")
MOD = 1000000007
mod = 998244353

n = I()
A = LI()
B = LI()
dp = [[0]*3005 for _ in range(3000)]
sdp = [[0]*3006 for _ in range(3000)]

for i in range(3005):
    if A[0] <= i <= B[0]:
        dp[0][i] = 1
    sdp[0][i+1] = sdp[0][i] + dp[0][i]

for i in range(1,n):
    for j in range(A[i], B[i]+1):
        dp[i][j] = sdp[i-1][j+1]
    for j in range(3005):
        sdp[i][j+1] = sdp[i][j] + dp[i][j]
        sdp[i][j+1] %= mod

ans = 0
for i in range(3005):
    ans += dp[n-1][i]
print(ans%mod)
