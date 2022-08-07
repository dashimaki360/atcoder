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
P = LI()
P = [0,0] + P
ans = 0
x = P[n]
while 1:
    x = P[x]
    ans += 1
    if x == 0:
        break
print(ans)
    


