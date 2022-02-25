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
A = LI()
cnt = [0] * 200
for i in range(n):
    cnt[A[i]%200] += 1
ans = 0
for c in cnt:
    if c < 2: continue
    ans += c*(c-1)//2
print(ans)
