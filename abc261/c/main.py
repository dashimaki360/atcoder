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
d = dict()
for i in range(n):
    s = input()
    if s not in d:
        print(s)
        d[s] = 1
    else:
        print( s+ "(" + str(d[s]) + ")")
        d[s] += 1

