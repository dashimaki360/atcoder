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

a,b,n = LI()

x = b-1
if x > n:
    x = n
ans = math.floor(a*x/b) - a*math.floor(x/b)
print(ans)

