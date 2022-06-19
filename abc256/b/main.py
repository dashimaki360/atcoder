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

n = I()
A = LI()

p = 0
base = [0]*4
for a in A:
    base[0] = 1
    tmp = base.copy()
    base = [0]*4
    for i in range(4):
        if a+i > 3:
            p += tmp[i]
        else:
            base[a+i] = tmp[i]
print(p)
    

