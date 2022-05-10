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
from collections import deque

n,x = LI()
S = input()

q = list(map(int, list(bin(x)[2:])))
for s in S:
    if s == "U":
        q.pop()
    elif s == "L":
        q.append(0)
    elif s == "R":
        q.append(1)

ans = 0
for i in q:
    ans = 2*ans + i
print(ans)
