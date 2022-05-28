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

n,m,q = LI()
Q = [LI() for _ in range(n)]
q3 = [[] for _ in range(n)]
for qi in reversed(range(q):
    if Q[qi][0] == 1:
        pass
    elif Q[qi][0] == 2:
        pass
    else:
        i = Q[qi][1] -1
        j = Q[qi][2] -1
        q3[i].append(j)
        

