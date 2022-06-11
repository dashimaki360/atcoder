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

cnt = [[0]*10 for _ in range(10)]
for i in range(1,n+1):
    top = int(str(i)[0])
    end = i%10
    cnt[top][end] += 1

ans = 0
for top in range(1,10):
    for end in range(1,10):
        ans += cnt[top][end] * cnt[end][top]

print(ans)
