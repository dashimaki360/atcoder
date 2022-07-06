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

n,P,K = LI()
A = []
for _ in range(n):
    A.append(LI())

def solve(x):
    cost = [[INF]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            cost[i][j] = A[i][j] if A[i][j] != -1 else x
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                cost[i][j] = min(cost[i][j], cost[i][k]+cost[k][j])
    cnt = 0
    for i in range(n):
        for j in range(i+1,n):
            if cost[i][j] <= P:
                cnt += 1
    return cnt


if solve(INF) == K:
    print("Infinity")
    exit()
if solve(1) < K:
    print(0)
    exit()

l = 1; r = INF
if solve(1) == K:
    ll = 1
else:
    while r - l > 1:
        x = (l + r)//2
        if solve(x) > K:
            l = x
        else:
            r = x
    ll = r

l = 1; r = INF
while r - l > 1:
    x = (l + r)//2
    if solve(x) >= K:
        l = x
    else:
        r = x

rr = r
ans = rr - ll
print(ans)

