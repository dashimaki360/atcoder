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

ans = -1
r = 0
kind = defaultdict(int)

def is_ok():
    if r >= n:
        return False
    x = len(kind)
    if A[r] not in kind:
        x += 1
    return  x <= k

for l in range(n):
    while is_ok():
        kind[A[r]] += 1
        r += 1
    ans = max(ans, r-l)
    if l == r:
        r += 1
    else:
        kind[A[l]] -= 1
        if kind[A[l]] <= 0:
            kind.pop(A[l])
    # print(kind)
print(ans)


