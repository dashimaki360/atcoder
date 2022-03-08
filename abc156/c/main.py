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

n = I()
x = LI()
ans = math.inf
for i in range(105):
    cost = 0
    for xx in x:
        cost += (xx-i)**2
    ans = min(ans, cost)
print(ans)
