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
B = A[k:]
A = A[:k]
#mk = min(A)
maxb = max(B)

# print(A)
# print(B)
# print(mk)
C = [0]*(n-k)
for i in range(n-k):
    if i == 0: C[0] = B[0]
    else: C[i] = max(C[i-1], B[i])
# print(B)
# print(C)
ans = INF 
for i, a  in enumerate(A):
    if maxb <= a: continue
    x = bisect.bisect_right(C, a)
    ans = min(k-i+x, ans)
if ans == INF:
    ans = -1
print(ans)

