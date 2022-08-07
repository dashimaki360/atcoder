#!/usr/bin/env python3
import sys, math ,heapq, bisect
from collections import deque
sys.setrecursionlimit(10**6)
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def yes(): print("Yes")
def no(): print("No")
MOD = 998244353
INF = 10**18



n,m,k = LI()

graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = LI()
    a -= 1
    b -= 1
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)  # 有向グラフなら消す

odd = 0
for g in graph:
    if len(g)%2 == 1:
        odd += 1

comb_odd = [1]*(k+1)
comb_even = [1]*(k+1)
de = [1]*(k+1)
for i in range(k):
    comb_odd[i+1] = comb_odd[i] * (odd-i) % MOD
    comb_even[i+1] = comb_even[i] * (n-odd-i) % MOD
    de[i+1] = de[i] * (i+1) % MOD

ans = 0
for i in range(0,odd+1,2):
    if k-i < 0: continue
    if n-odd < k-i: continue
    ans += comb_odd[i]*pow(de[i],MOD-2,MOD) * comb_even[k-i]*pow(de[k-i],MOD-2,MOD)
    ans %= MOD
print(ans)

