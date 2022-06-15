#!/usr/bin/env python3
import sys, math ,heapq, bisect
from collections import deque
sys.setrecursionlimit(10**6)
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def yes(): print("Yes")
def no(): print("No")
MOD = 1000000007
INF = 10**18


fact = [0]*100009
factinv = [0]*100009
def init():
    fact[0] = 1
    for i in range(1,100009):
        fact[i] = (i*fact[i-1]) % MOD
    for i in range(100009):
        factinv[i] = pow(fact[i], MOD-2, MOD)

def comb(n, r):
    return fact[n] * factinv[r] * factinv[n-r] % MOD

n = I()
init()
for k in range(1,n+1):
    ans = 0
    for ball in range(1,n+1):
        if k*(ball-1)+1 > n: break
        ans += comb(n-(k-1)*(ball-1), ball)
        ans %= MOD
    print(ans)
        
