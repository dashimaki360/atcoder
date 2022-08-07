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

A = LI()
A.sort()
if A[0] == A[1] == A[2] and A[3] == A[4]:
    yes()
elif A[0] == A[1] and A[2] == A[3] == A[4]:
    yes()
else:
    no()
