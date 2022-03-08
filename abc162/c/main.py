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
import itertools

k = I()
ans = 0
it = itertools.product(range(1,k+1), repeat=3)
for a,b,c in it:
    ans += math.gcd(math.gcd(a,b),c)
print(ans)

