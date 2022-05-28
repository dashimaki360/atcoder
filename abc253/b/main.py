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

h,w = LI()
A = []
for i in range(h):
    s = input()
    for j in range(w):
        if s[j] == 'o':
            A.append([i,j])

ans = abs(A[0][0]-A[1][0]) + abs(A[0][1]-A[1][1])
print(ans)



    

