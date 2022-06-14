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

n,k = LI()
s = input()

cnt = [[-1]*26 for _ in range(n)]
for i in range(n-1,-1,-1):
    if i+1 < n:
        for j in range(26):
            cnt[i][j] = cnt[i+1][j]
    x = ord(s[i]) - ord('a')
    cnt[i][x] = i
    
pos = 0
ans = []
while len(ans) < k:
    for i in range(26):
        if cnt[pos][i] == -1: continue
        if cnt[pos][i] <= n-k+len(ans):
            ans.append(i)
            pos = cnt[pos][i]+1
            break
    else:
        assert False, "error"
for i in range(k):
    ans[i] = ans[i]+ord("a")
    ans[i] = chr(ans[i])
print("".join(ans))

