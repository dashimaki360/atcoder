#!/usr/bin/env python3
import sys, math ,heapq, bisect
from collections import deque, defaultdict
sys.setrecursionlimit(10**6)
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def yes(): print("Yes")
def no(): print("No")
MOD = 998244353
INF = 10**18

n,k = LI()
A = LI()

ans = 0
for i in range(n):
    for j in range(i, n):
        if len(set(A[i:j+1])) <= k:
            ans = max(ans, j-i+1)
print(ans)