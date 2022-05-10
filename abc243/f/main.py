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
MOD = 998244353
mod = 998244353
INF = 10**18

n,m,k = LI()
W = []
for i in range(n):
    W.append(I())
N = 1<<n
WSUM = pow(sum(W), k, MOD)

ans = 0
for i in range(N):
    w = 0
    popcnt = bin(i).count("1")
    if popcnt > m:
        continue
    for j in range(n):
        if i>>j & 1:
            w += W[j]
    w = pow(w,k,MOD)
    if (m - popcnt) % 2:
        w = -w
    ans += w
    ans %= MOD

ans *= pow(WSUM, MOD-2, MOD)
ans %= MOD
print(ans)
