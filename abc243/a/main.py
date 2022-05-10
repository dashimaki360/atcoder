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

v,a,b,c = LI()
while 1:
    v -= a
    if v < 0:
        print("F")
        break
    v -= b
    if v < 0:
        print("M")
        break
    v -= c
    if v < 0:
        print("T")
        break
