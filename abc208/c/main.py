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

n,k = LI()
A = LI()
l = [[A[i], i] for i in range(n)]
ans = [k//n]*n
l.sort()
for i in range(k%n):
    ans[l[i][1]] += 1
for an in ans:
    print(an)


