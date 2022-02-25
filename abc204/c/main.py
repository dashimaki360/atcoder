#!/usr/bin/env python3
import sys, math
sys.setrecursionlimit(10**6)
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def yes(): print("Yes")
def no(): print("No")
MOD = 1000000007
from collections import deque

n,m = LI()
l = [[] for _ in range(n)]
for i in range(m):
    a,b = LI()
    a -= 1
    b -= 1
    l[a].append(b)
ans = 0
for st in range(n):
    reach = [0]*n
    reach[st] = 1
    d = deque()
    d.append(st)
    while d:
        v = d.popleft()
        for i in l[v]:
            if reach[i] == 1:
                continue
            reach[i] = 1
            d.append(i)
    ans += sum(reach)
print(ans)

