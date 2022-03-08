#!/usr/bin/env python3
import sys, math
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def yes(): print("Yes")
def no(): print("No")
MOD = 1000000007

n,k = LI()
A = LI()

def is_ok(x):
    tmp = 0
    for a in A:
        tmp += min(x,a)
    if tmp >= x*k:
        return True
    else:
        return False

ok = 0
ng = 10**18
while ng-ok > 1:
    nxt = (ok+ng)//2
    if is_ok(nxt):
        ok = nxt
    else:
        ng = nxt
print(ok)



