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
L = [0]*n
R = [0]*n
for i in range(n):
    l,r = LI()
    L[i] = l
    R[i] = r
ans = 0
for i in range(n):
    for j in range(i):
        tmp = 0
        all = (R[j] - L[j] + 1)*(R[i] - L[i] + 1)
        for a in range(L[j], R[j]+1):
            for b in range(L[i], R[i]+1):
                if a > b: tmp += 1
        ans += tmp / all
print(ans)
        
            
        
