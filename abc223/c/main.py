#!/usr/bin/env python3
import sys, math
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def yes(): print("Yes")
def no(): print("No")
MOD = 1000000007

n = I()
A = [LI() for _ in range(n)]
s = 0.0
for a,b in A:
    s += a/b
x = 0
l = 0
for a,b in A:
    x += a/b
    l += a
    if x >= s/2:
        y = x - s/2
        ans = (l-b*y)
        print(ans)
        break

