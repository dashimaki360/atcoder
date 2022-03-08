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

s = S()
k = I()
n = len(s)
a = [0]*n

for i in range(n):
    if s[i] == '.':
        a[i] = 1
r = 0
sum = 0
ans = 0
# [l, r)
for l in range(n):
    while r < n and sum + a[r] <= k:
        sum += a[r]
        r += 1
    ans = max(ans, r-l)
    sum -= a[l]
print(ans)





