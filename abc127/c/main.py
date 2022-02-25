#!/usr/bin/env python3
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def yes(): print("Yes")
def no(): print("No")


#n,m = map(int, input().split())
n,m = LI()
L = 0
R = n+100
for i in range(m):
    l,r = LI()
    L = max(L, l)
    R = min(R, r)
print(max(0,R-L+1))
