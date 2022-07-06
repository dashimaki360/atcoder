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

n,q = LI()
L = []
for _ in range(q):
    x,y,z,w = LI()
    L.append([x-1, y-1, z-1, w])

ans = 1
for rank in range(60):
    tmp = 0
    for k in range(1<<n):
        for x,y,z,w in L:
            if k>>x&1 | k>>y&1 | k>>z&1 != w>>rank&1:
                break
        else:
            tmp += 1
    ans *= tmp
    ans %= MOD
print(ans)





