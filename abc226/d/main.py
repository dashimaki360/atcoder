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
from collections import defaultdict

n = I()
xy = [LI() for _ in range(n)]

# d = defaultdict(int)
d = set()

for i in range(n):
    for j in range(n):
        if i == j: continue
        dx = xy[i][0] - xy[j][0]
        dy = xy[i][1] - xy[j][1]
        a = math.gcd(dx,dy)
        dx = dx//a
        dy = dy//a
        d.add((dx,dy))
ans = len(d)
print(ans)



