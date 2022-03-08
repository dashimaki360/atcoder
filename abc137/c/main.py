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
d = defaultdict(int)
for i in range(n):
    s = input()
    d["".join(sorted(s))] += 1

ans = 0
for i in d.values():
    if i >1:
        ans += i*(i-1)//2
print(ans)
