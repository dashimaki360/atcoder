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
A = [S() for _ in range(n)]
d = defaultdict(int)
for a in A:
    d[a] += 1
d = sorted(d.items(), key=lambda x:x[1], reverse=True)
m = d[0][1]
ans = []
for dd in d:
    if dd[1] != m:
        break
    ans.append(dd[0])
ans.sort()
for an in ans:
    print(an)

