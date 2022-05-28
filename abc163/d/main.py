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

ans = 0
for i in range(k,n+2):
    ans += (n+n-i+1)*i//2 - (i-1)*i//2 + 1
    ans %= MOD
    # print(ans, i)
print(ans)


