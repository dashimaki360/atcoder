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

s = [0]*n
for i in range(1<<n):
    cnt = 0
    for j in range(n):
        if i&1:
            s[-j-1] = ")"
            cnt += 1
        else:
            s[-j-1] = "("
            cnt -= 1
        i = i>>1
        if cnt < 0: break
    else:
        if cnt == 0:
            print("".join(s))




