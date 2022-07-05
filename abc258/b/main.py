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

n = int(input())
A = []
for i in range(n):
    A.append(input())

delta = ((1,0),(-1,0),
         (0,1),(0,-1),
         (1,1),(-1,-1),
         (1,-1),(-1,1)
        )

ans = -INF
for dx, dy in delta:
    for st_i in range(n):
        for st_j in range(n):
            tmp = 0
            for step in range(n):
                x = (st_i+dx*step)%n
                y = (st_j+dy*step)%n
                tmp *= 10
                tmp += int(A[x][y])
            ans = max(ans, tmp)
print(ans)

