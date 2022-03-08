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
mod = 998244353

n = I()
dp = [1] * 10
dp[0] = 0
for i in range(1,n):
    tmp = dp.copy()
    dp[1] = (tmp[1] + tmp[2])%mod
    dp[2] = (tmp[1] + tmp[2] + tmp[3])%mod
    dp[3] = (tmp[2] + tmp[3] + tmp[4])%mod
    dp[4] = (tmp[3] + tmp[4] + tmp[5])%mod
    dp[5] = (tmp[4] + tmp[5] + tmp[6])%mod
    dp[6] = (tmp[5] + tmp[6] + tmp[7])%mod
    dp[7] = (tmp[6] + tmp[7] + tmp[8])%mod
    dp[8] = (tmp[7] + tmp[8] + tmp[9])%mod
    dp[9] = (tmp[8] + tmp[9])%mod

ans = sum(dp)%mod
print(ans)


