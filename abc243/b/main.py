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

n = I()
A = LI()
B = LI()

ans1 = []
for i in range(n):
    if A[i] == B[i]:
        ans1.append(A[i])
ans2 = []
for i in range(n):
    x = A[i]
    if x in B and not x in ans1:
        ans2.append(x)

print(len(ans1))
print(len(ans2))
