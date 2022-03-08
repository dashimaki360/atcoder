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
A = LI()

dp = [[0]*10 for _ in range(n)]
dp[0][A[0]] = 1
for i in range(n-1):
    for num in range(10):
        a = num; b = A[i+1]
        dp[i+1][(a+b)%10] += dp[i][a]%mod
        dp[i+1][(a*b)%10] += dp[i][a]%mod

# print(dp)
ans = dp[n-1]
for an in ans:
    print(an%mod)

