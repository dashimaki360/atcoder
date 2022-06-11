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

n = I()
A = LI()
cnt = [0]*61

for a in A:
    for i in range(60):
        if a>>i&1:
            cnt[i] += 1
ans = 0
for i, c in enumerate(cnt):
    ans += c*(n-c)*pow(2,i,MOD)
    ans %= MOD
print(ans%MOD)