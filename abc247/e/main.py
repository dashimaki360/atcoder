#!/usr/bin/env python3
import sys, math ,heapq, bisect
from collections import deque
from telnetlib import XASCII
sys.setrecursionlimit(10**6)
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def yes(): print("Yes")
def no(): print("No")
MOD = 1000000007
INF = 10**18

n,x,y = LI()
A = LI()
xs = []
ys = []
out = []
for i,a in enumerate(A):
    if a == x:
        xs.append(i)
    if a == y:
        ys.append(i)
    if a > x or a < y:
        out.append(i)
xs.append(INF)
ys.append(INF)
out.append(n)

ans = 0
minx = 0
miny = 0
minout = 0
for l in range(n):
    rnum = max(0, out[minout] - max(xs[minx], ys[miny]))
    # print(xs[minx], ys[miny], out[minout])
    # print(rnum)
    ans += rnum
    if l == xs[minx]: minx+=1
    if l == ys[miny]: miny+=1
    if l == out[minout]: minout+=1
print(ans)


