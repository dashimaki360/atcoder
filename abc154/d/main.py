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

n,k = LI()
A = LI()
sum = [0] * (n+1)
for i in range(n):
    sum[i+1] = sum[i] + A[i]

ans = 0
for i in range(n):
    if i+k > n:
        continue
    ans = max(ans, sum[i+k] - sum[i])
print((ans+k)/2)


