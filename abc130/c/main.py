#!/usr/bin/env python3
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def yes(): print("Yes")
def no(): print("No")

w,h,x,y = LI()
s = w*h/2
if x == w/2 and y == h/2:
    a = 1
else:
    a = 0
print(s,a)