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
low = 0
high = (1<<30) - 1


ans = c
for _ in range(n):
    t,a = LI()
    if t == 1:
        low &= a
        high &= a
    elif t == 2:
        low |= a
        high |= a
    elif t == 3:
        low ^= a
        high ^= a
    
    # print(high, low, ans)

    ans = (ans&high) + ((~ans)&low)
    print(ans)
