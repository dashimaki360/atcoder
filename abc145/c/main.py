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
import itertools

n = I()
A = [LI() for _ in range(n)]
it = itertools.permutations(range(n),n)
ans = 0
nn = 0
for x in it:
    nn += 1
    at = x[0]
    for i in range(1,n):
        to = x[i]
        ans += ((A[at][0]-A[to][0])**2 + (A[at][1] - A[to][1])**2)**0.5
        at = to
ans = ans/nn
print(ans)


