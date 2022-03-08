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

n,k,q= LI()
point = [-q+k]*n
for i in range(q):
    a = I()
    a -= 1
    point[a] += 1

for p in point:
    if p > 0:
        yes()
    else:
        no()
