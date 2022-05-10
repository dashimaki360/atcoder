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

n,k = LI()
A = LI()
B = LI()
AA = [False]*n
BB = [False]*n
AA[0] = True
BB[0] = True

for i in range(1,n):
    if AA[i-1] == True:
        if abs(A[i-1] - A[i]) <= k:
            AA[i] = True
        if abs(A[i-1] - B[i]) <= k:
            BB[i] = True
    if BB[i-1] == True:
        if abs(B[i-1] - A[i]) <= k:
            AA[i] = True
        if abs(B[i-1] - B[i]) <= k:
            BB[i] = True
if AA[n-1] or BB[n-1]:
    yes()
else:
    no()
