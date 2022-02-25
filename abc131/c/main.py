#!/usr/bin/env python3
import math
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def yes(): print("Yes")
def no(): print("No")

a,b,c,d = LI()
def solve(x):
    a = x//c + x//d - x//(c*d//math.gcd(c,d))
    return x - a

ans = solve(b) - solve(a-1)
print(ans)

