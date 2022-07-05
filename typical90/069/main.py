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
MOD = 1000000007
INF = 10**18

n,k = LI()

if n == 1:
    print(k)
    exit()
elif n == 2:
    print((k*(k-1))%MOD)
    exit()

ans = k
ans *= k-1
ans *= pow(k-2, n-2, MOD)
ans %= MOD
print(ans)

