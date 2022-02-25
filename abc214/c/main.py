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

n = I()
t = LI()
s = LI()
a = s.index(min(s))
ans = [-1]*n
ans[a] = s[a]
for i in range(n):
    pre = a
    a = (a+1)%n
    ans[a] = min(s[a], ans[pre]+t[pre])

for i in range(n):
    print(ans[i])