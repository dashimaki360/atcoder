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


k = I()
l = []
for i in range(1,k+1):
    if i*i > k: break
    if k%i == 0:
        l.append(i)
        if k//i != i:
            l.append(k//i)

l.sort()
ans = 0
for a in l:
    for b in l:
        if a>b: continue
        if k%(a*b): continue
        c = k//(a*b)
        if b > c: continue
        ans += 1
print(ans)


