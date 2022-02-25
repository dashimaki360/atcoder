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

def g1(x):
    return int("".join(sorted(str(x), reverse=True)))
def g2(x):
    return int("".join(sorted(str(x), reverse=False)))

def f(x):
    return g1(x)-g2(x)

n,k = LI()
ans = n
for _ in range(k):
    ans = f(ans)
print(ans)


