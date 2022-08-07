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

n,m = LI()

x = [0]*n

def dfs(c):
    if c == n:
        print(" ".join(map(str,x)))
        return
    for i in range(c+1,m+1):
        if c > 0 and x[c-1] >= i: continue
        x[c] = i
        dfs(c+1)

dfs(0)



