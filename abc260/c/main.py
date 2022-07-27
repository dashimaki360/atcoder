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

n,x,y = LI()
R = [0]*11
B = [0]*11
R[n] = 1

for i in range(10,1,-1):
    if i < 2: break
    R[i-1] += R[i]
    B[i] += R[i] * x
    R[i] = 0
    R[i-1] += B[i]
    B[i-1] += B[i]*y
ans = B[1]
print(ans)

