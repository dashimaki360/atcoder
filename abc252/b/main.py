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

n,k = LI()
A = LI()
B = LI()
maxa = []
max = 0
for i in range(n):
    if max < A[i]:
        max = A[i]
        maxa = []
        maxa.append(i+1)
    elif max == A[i]:
        maxa.append(i+1)

for b in B:
    if b in maxa:
        yes()
        break
else:
    no()

