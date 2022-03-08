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
mod = 998244353
ord_A = 65

def bad_s(n,s):
    if n%2 == 0:
        head = s[:(n)//2]
        tail = s[(n)//2:]
    else:
        head = s[:(n+1)//2]
        tail = s[(n+1)//2-1:]
    head = head[::-1]
    # print(head, tail)
    # print(head, tail, tail<head)
    return tail < head

def solve():
    n = I()
    s = S()
    ans = 0

    if n == 1:
        print(ord(s)-ord_A+1)
        return

    # dp = [0]*2
    # dp[0] = 0
    # dp[1] = 1
    for c in s[:(n+1)//2]:
        ans = ans*26 + (ord(c)-ord_A)
        ans %= mod
    if not bad_s(n,s):
        ans += 1 
    print(ans%mod)

t = I()
for i in range(t):
    solve()
