#!/usr/bin/env python3
import sys, math ,heapq, bisect
from collections import deque
sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def yes(): print("Yes")
def no(): print("No")
MOD = 1000000007
INF = 10**18

n = I()
A = LI()
st = 0
flip = 0
while len(A) - st > 1:
    if A[-1] == flip:
        A.pop()
        continue
    if A[st] == flip:
        flip = (flip+1)%2
        st += 1
        continue
    no()
    exit()
if A[-1] == flip:
    yes()
else:
    no()