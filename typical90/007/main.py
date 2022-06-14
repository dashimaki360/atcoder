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

n = I()
A = LI()
q = I()
A.append(INF)
A.append(INF)
A.append(-INF)
A.append(-INF)
A.sort()
for _ in range(q):
    b = I()
    i = bisect.bisect_left(A,b)
    ans = min(abs(b-A[i-1]),abs(b-A[i]))
    print(ans)
