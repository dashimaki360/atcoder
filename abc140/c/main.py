#!/usr/bin/env python3
import enum
import sys, math
sys.setrecursionlimit(10**6)
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def yes(): print("Yes")
def no(): print("No")
MOD = 1000000007

n = I()
B = LI()
ans = 0
pre = math.inf
for i,b in enumerate(B):
    ans += min(pre,b)
    pre = b
ans += pre
print(ans)

