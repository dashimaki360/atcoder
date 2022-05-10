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

n,q = LI()
A = LI()
B = [0]*n
for i,a in enumerate(A):
    B[i] = a - i - 1

def solve(x):
    if x > B[-1]:
        ans = A[-1] + k - B[-1]
        print(ans)
    else:
        p = bisect.bisect_left(B,x)
        ans = (A[p] - 1) - (B[p] - x)
        print(ans)

for _ in range(q):
    k = I()
    solve(k)
