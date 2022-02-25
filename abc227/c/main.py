#!/usr/bin/env python3
import sys, math
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def yes(): print("Yes")
def no(): print("No")
MOD = 1000000007

n = I()

amax = int(n**(1/3))+10
bmax = int(n**(1/2))+10
ans = 0
for a in range(1, amax):
    for b in range(a, bmax):
        x = n//(a*b)
        if x-b < 0:
            break
        else:
            ans += x-b+1
print(ans)