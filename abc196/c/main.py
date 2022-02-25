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

ns = input()
n = int(ns)
i = len(ns)//2
if i == 0:
    print(0)
    exit()
ans = 10**i - 1
a = n//(10**i)
b = n%(10**i)
if a <= b:
    ans = min(ans, a)
else:
    ans = min(ans, a-1)
print(ans)


