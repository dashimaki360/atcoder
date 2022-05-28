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

if x < a*a*b/2:
    ans = math.atan(x/(a*b*b*0.5)) / math.pi * 180
    ans = 90 - ans
else:
    ans = math.atan((a*a*b-x)/(a*a*a*0.5)) / math.pi * 180
print(ans)



