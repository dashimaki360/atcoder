#!/usr/bin/env python3
import sys, math ,heapq, bisect
from collections import deque
sys.setrecursionlimit(10**6)
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def yes(): print("Yes")
def no(): print("No")
MOD = 1000000007
INF = 10**18

n,c = LI()
tmp = [[0]*2 for _ in range(30)]
for i in range(30):
    tmp[i][1] = 1
ans = c
for _ in range(n):
    t,a = LI()
    if t == 1:
        for i in range(30):
            tmp[i][0] &= a>>i&1
            tmp[i][1] &= a>>i&1
    elif t == 2:
        for i in range(30):
            tmp[i][0] |= a>>i&1
            tmp[i][1] |= a>>i&1
    elif t == 3:
        for i in range(30):
            tmp[i][0] ^= a>>i&1
            tmp[i][1] ^= a>>i&1

    # print(tmp)
    x = 0
    for i in range(30):
        y = tmp[i][ans>>i&1]
        x += y<<i
    ans = x
    print(ans)
