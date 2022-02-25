#!/usr/bin/env python3
import sys, math
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def yes(): print("Yes")
def no(): print("No")
MOD = 1000000007

n,q = LI()
A = LI()
d = dict()
for i, a in enumerate(A):
    if a in d:
        d[a].append(i+1)
    else:
        d[a] = [i+1]
for i in range(q):
    x,k = LI()
    if not x in d:
        print(-1)
    elif k > len(d[x]):
        print(-1)
    else:
        print(d[x][k-1])
