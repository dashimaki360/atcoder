#!/usr/bin/env python3
import sys, math
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def yes(): print("Yes")
def no(): print("No")
MOD = 1000000007


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

def nHk(n,k,mod):
    return comb(n+k-1, k, mod)

n,k = LI()

def solve(i):
    b = k-i
    r = n-k-i+1
    # blue = comb(b+i-1, b, MOD)
    # red = comb(r+i, r, MOD)
    blue = nHk(i,b,MOD)
    red = nHk(i+1,r,MOD)
    print((blue*red)%MOD)

for i in range(1,k+1):
    solve(i)

