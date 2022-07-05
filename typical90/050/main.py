#!/usr/bin/env python3
import sys, math ,heapq, bisect
from collections import deque
sys.setrecursionlimit(10**6)
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def yes(): print("Yes")
def no(): print("No")
MOD = 1000000007
INF = 10**18

n,l = LI()

dp = [0]*(n+l+5)
dp[0] = 1
for i in range(n):
    dp[i+1] += dp[i]
    dp[i+l] += dp[i]
print(dp[n]%MOD)
    
