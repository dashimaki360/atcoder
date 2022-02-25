#!/usr/bin/env python3
import sys, math
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def yes(): print("Yes")
def no(): print("No")
MOD = 1000000007

l,r = LI()
r = min(l+2500, r)
ans = 1001001
for i in range(l, r+1):
    for j in range(i+1, r+1):
        ans = min(ans, (i*j)%2019)
print(ans)



