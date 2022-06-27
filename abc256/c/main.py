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

h1,h2,h3,w1,w2,w3 = LI()

ans = 0
for a in range(1,30):
    for b in range(1,30):
        for d in range(1,30):
            for e in range(1,30):
                c = w1 - a - b
                f = w2 - d - e
                g = h1 - a - d
                h = h2 - b - e
                i = h3 - c - f
                i2 = w3 - g - h
                if min(c,f,g,h,i,i2) <= 0: continue
                if i != i2: continue
                ans += 1
print(ans)

