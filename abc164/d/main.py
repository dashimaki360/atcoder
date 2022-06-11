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

s = list(map(int, (reversed(input()))))
cnt = [0]*2019
x = 1
tot = 0
cnt[0] += 1
for i, ss in enumerate(s):
    tot += ss * x
    x = x*10%2019
    tot %= 2019
    cnt[tot] += 1
ans = 0
for c in cnt:
    ans += c*(c-1)//2
print(ans)
