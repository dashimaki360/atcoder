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

ans = [0]*n
ans[0] = 1
for i in range(n):
    if i-1 < 0:
        print(*ans[:(i+1)])
        continue
    tmp = ans.copy()
    for j in range(1,n):
        ans[j] = tmp[j-1]+tmp[j]
    print(*ans[:(i+1)])
    
    

