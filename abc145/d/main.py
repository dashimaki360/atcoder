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

from numpy.linalg import solve
 

x,y = LI()
#2*a + b = x
#a + 2*b = y
if (y+x) % 3:
    print(0)
    exit()

left = [[1, 2],
        [2, 1]]
right = [x, y]
a,b = map(int, solve(left, right))

def comb(n, r, mod):
    # mod素数のときつかえる
    # 素数でないときは拡張ユークリッドの互除法で逆元もとめること
    if n < 0 or r < 0 or r > n: return 0
    nu = 1
    de = 1
    for i in range(r):
        nu = nu * (n-i) % mod
        de = de * (i+1) % mod
    return nu * pow(de,mod-2,mod) % mod

ans = comb(a+b, a, MOD)
print(ans)