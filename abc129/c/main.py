#!/usr/bin/env python3
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def yes(): print("Yes")
def no(): print("No")
mod = 1000000007

n,m = LI()
#A = [int(input()) for _ in range(m)]
A = [int(input()) for _ in range(m)]
A = set(A)
dp = [0]*(n+1)
dp[0] = 1
if 1 in A:
    dp[1] = 0
else:
    dp[1] = 1

for i in range(2,n+1):
    if i in A:
        dp[i] = 0
    else:
        dp[i] = (dp[i-2] + dp[i-1]) % mod
ans = dp[n] % mod
print(ans)