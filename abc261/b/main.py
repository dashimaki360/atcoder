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
A = [ input() for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j: continue
        a = A[i][j]
        b = A[j][i]
        if a == "W" and b == "L":
            pass
        elif a == "L" and b == "W":
            pass
        elif a == "D" and b == "D":
            pass
        else:
            print("incorrect")
            exit()
print("correct")
