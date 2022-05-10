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
INF = 10**18

n = I()
m = 1000000

def sieve_of_eratosthenes(n):
    prime = [True for i in range(n+1)]
    prime[0] = False
    prime[1] = False

    sqrt_n = math.ceil(math.sqrt(n))
    for i in range(2, sqrt_n):
        if prime[i]:
            for j in range(2*i, n+1, i):
                prime[j] = False

    return prime

prime = sieve_of_eratosthenes(m)
pl = []
ans = 0
for p in range(m):
    if prime[p]:
        pl.append(p)

for p in range(len(pl)):
    if pl[p]*(pl[p+1]**3) > n:
        break
    ok = p+1
    ng = len(pl)
    while ng-ok > 1:
        x = (ok+ng)//2
        if pl[p] * (pl[x]**3) <= n:
            ok = x
        else:
            ng = x
    ans += ok - p
print(ans)