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

s = input()
m = I()

s = (list(map(int,list(s))))
maxs = max(s)
ok = 0
ng = m+1

def is_ok(x):
    if x == 0: return True
    if x == 1: return True
    tmp = 0
    for i, a in enumerate(reversed(s)):
        tmp += a*(x**i)
    return tmp <= m

if len(s) == 1:
    if s[0] <= m:
        print(1)
    else:
        print(0)
    exit()

while ng-ok > 1:
    x = (ng+ok)//2
    if is_ok(x):
        ok = x
    else:
        ng = x

ans = max(0, ok-maxs)
print(ans)

