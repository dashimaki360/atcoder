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

n,m = LI()
AB = [[] for _ in range(m+1)]
for i in range(n):
    a,b = LI()
    if a > m: continue
    AB[a].append(-b)

ans = 0
import heapq  # heapqライブラリのimport
que = []
heapq.heapify(que) # リストを優先度付きキューへ
for i in range(1,m+1):
    for val in AB[i]:
        heapq.heappush(que, val)
    if len(que) > 0:
        x  = -heapq.heappop(que)
        ans += x
print(ans)