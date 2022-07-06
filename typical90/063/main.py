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

h,w = LI()
P = []
for _ in range(h):
    P.append(LI())

ans = 0
for i in range(1<<8):
    tmp = [0]*w
    row = 0
    for j in range(h):
        if i>>j&1 == 0: continue
        row += 1
        for k in range(w):
            if tmp[k] == -1: continue
            if tmp[k] == 0:
                tmp[k] = P[j][k]
            elif tmp[k] != P[j][k]:
                tmp[k] = -1
    cnt = [0]*(h*w+5)
    for t in tmp:
        if t < 1: continue
        cnt[t] += 1
    x = max(cnt)
    ans = max(ans, x*row)
print(ans)