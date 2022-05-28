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
MOD = 998244353
INF = 10**18

n = I()
A = LI()
cnt = [0] * (n+1)
for a in A:
    cnt[a] += 1
tot = 0
for c in cnt:
    tot += c*(c-1)//2
for a in A:
    ans = tot - cnt[a]*(cnt[a]-1)//2 + (cnt[a]-1)*(cnt[a]-2)//2
    print(ans)

