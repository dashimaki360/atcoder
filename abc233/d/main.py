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

n,k = LI()
a = LI()
asum = [0] * (n+1)
for i in range(n):
    asum[i+1] = asum[i] + a[i]
d = defaultdict(int)
ans = 0
for i in range(n):
    d[asum[i]] += 1
    ans += d[asum[i+1]-k]
print(ans)

    


