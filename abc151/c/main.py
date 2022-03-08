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
A = [LS() for _ in range(m)]

ans = [0,0]
l = [False]*n
wa = [0]*n
for p,s in A:
    p = int(p) -1
    if l[p]:
        continue
    if s == "AC":
        l[p] = True
        ans[0] += 1
        ans[1] += wa[p]
    if s == "WA":
        wa[p] += 1
print(*ans)
