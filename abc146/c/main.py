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

a,b,x = LI()
ok = 0
ng = 1001001001
while ok != ng-1:
    n = (ok+ng)//2
    if x >= a*n + b*len(str(n)):
        ok = n
    else:
        ng = n
print(min(10**9, ok))

