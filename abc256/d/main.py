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
A = [0]*(200005)
for _ in range(n):
    l,r = LI()
    A[l] += 1
    A[r] -= 1

cnt = 0
st = -1
for i,a in enumerate(A):
    cnt += a
    if st == -1 and cnt > 0:
        st = i
    if st > 0 and cnt == 0:
        print(st, i)
        st = -1

    

