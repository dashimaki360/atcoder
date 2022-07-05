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
C = LI()

mc = min(C)
a = n//mc
b = n%mc

ans = ""
for i in [9,8,7,6,5,4,3,2,1]:
    c = C[i-1]
    if mc == c:
        ans += str(i) * a
        break
    while b >= c - mc:
        ans += str(i)
        b -= c-mc

print(ans[:a])


