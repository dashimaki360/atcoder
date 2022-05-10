#!/usr/bin/env python3
import sys, math ,heapq, bisect
from collections import deque
sys.setrecursionlimit(10**6)
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def yes(): print("Yes")
def no(): print("No")
MOD = 998244353
INF = 10**18

n,a,b = LI()
ans = [["."]*(a*n) for _ in range(b*n)]
for i in range(n):
    s = ""
    for j in range(n):
        if (j+i)%2:
            s += "#"*b
        else:
            s += "."*b
    for _ in range(a):
        print(s)

