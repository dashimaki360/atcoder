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
MOD = 1000000007
INF = 10**18

from collections import defaultdict
n = I()
XY = [LI() for _ in range(n)]
S = input()

dr = dict()
dl = defaultdict(int)
for i in range(n):
    x,y = XY[i]
    if S[i] == "L":
        dl[y] = max(dl[y], x)
    else:
        if not y in dr:
            dr[y] = x
        else:
            dr[y] = min(dr[y], x)

for y in dr:
    if not y in dl:
        continue
    if dr[y] <= dl[y]:
        yes()
        exit()
no()



