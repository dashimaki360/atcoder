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
B = LI()
C = LI()

def cnt(X):
    ret = [0]*46
    for x in X:
        ret[x%46] += 1
    return ret

cntA = cnt(A)
cntB = cnt(B)
cntC = cnt(C)

ans = 0
for i in range(46):
    for j in range(46):
        for k in range(46):
            if (i+j+k)%46: continue
            ans += cntA[i]*cntB[j]*cntC[k]
print(ans)            