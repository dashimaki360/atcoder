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
A = LI()

cnt = 0
for i in range(n):
    A[i] -= 1
    if A[i] == i:
        cnt += 1
ans = 0
ans += cnt*(cnt-1)//2

cnt2 = 0
for i in range(n):
    if A[i] == i: continue
    x = A[i]
    if A[x] == i:
        cnt2 += 1
ans += cnt2//2
# print(cnt, cnt2)
print(ans)
        
