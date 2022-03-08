#!/usr/bin/env python3
import sys, math
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def yes(): print("Yes")
def no(): print("No")
MOD = 1000000007
import itertools

n = I()
XY = [LI() for _ in range(n)]
s = set()
for x,y in XY:
    s.add((x,y))

ans = 0
it = itertools.combinations(range(n),2)
for i,j in it:
    x1, y1 = XY[i]
    x2, y2 = XY[j]
    if x1 == x2 or y1 == y2:
        continue
    if (x1,y2) in s and (x2,y1) in s:
        ans += 1
ans = ans//2
print(ans)


