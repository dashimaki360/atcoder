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

n,q = LI()
A = LI()

costs = [0]*(n-1)
ans = 0
for i in range(1,n):
    costs[i-1] = (A[i]-A[i-1])
    ans += abs(A[i-1]-A[i])

for _ in range(q):
    l,r,v = LI()
    l -= 1; r -=1
    if l > 0:
        ans -= abs(costs[l-1])
        costs[l-1] += v
        ans += abs(costs[l-1])
    if r < n-1:
        ans -= abs(costs[r])
        costs[r] -= v
        ans += abs(costs[r])
    print(ans)

