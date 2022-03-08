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

k,n = LI()
a = LI()
d_max = 0
for i in range(1,n):
    d = (a[(i+1)%n] - a[i])%k
    d_max = max(d_max, d)
print(k-d_max)