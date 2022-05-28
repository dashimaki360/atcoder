#!/usr/bin/env python3
import sys, math
sys.setrecursionlimit(10**6)
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def yes(): print("Yes")
def no(): print("No")
MOD = 1000000007
import heapq

n,m = LI()
A = LI()
for i in range(n): A[i] = -A[i]
heapq.heapify(A)
for i in range(m):
    x = heapq.heappop(A)*(-1)
    heapq.heappush(A, -(x//2))
print(-sum(A))


