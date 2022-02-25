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
A = LI()
d = defaultdict(int)
ans = 0
for i in range(n):
    ans += i - d[A[i]]
    d[A[i]] += 1
print(ans)

