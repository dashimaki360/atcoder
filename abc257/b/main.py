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

n,k,q= LI()
A = LI()
L = LI()
A.append(n+1)

for l in L:
    l -= 1
    if A[l]+1 != A[l+1]:
        A[l] += 1
A.pop()
print(*A)
