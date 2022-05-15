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

n = I()
d = dict()
for i in range(n):
    s,t = input().split()
    t = int(t)
    if s in d:
        continue 
    d[s] = [t, i+1]
ans = -1
maxt = 0
for t, i in d.values():
    if maxt < t:
        maxt = t
        ans = i
print(ans)
