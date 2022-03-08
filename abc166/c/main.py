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

n,m = LI()
h = LI()
A = [LI() for _ in range(m)]

ans = [1]*n
for a,b in A:
    a -=1
    b -=1
    if h[a] > h[b]:
        ans[b] = 0
    elif h[a] < h[b]:
        ans[a] = 0
    else:
        ans[a] = 0
        ans[b] = 0

ans = sum(ans)
print(ans)


