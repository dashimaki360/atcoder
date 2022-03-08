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
import heapq

n,m = LI()
AB = [LI() for _ in range(m)]
to = [[] for _ in range(n)]
ind = [0] * n

for a,b in AB:
    a -= 1; b -= 1
    to[a].append(b)
    ind[b] += 1
hq = []
for i in range(n):
    if ind[i] == 0:
        heapq.heappush(hq,i)
ans = []
while len(hq) > 0:
    i = heapq.heappop(hq)
    ans.append(i+1)
    for t in to[i]:
        ind[t] -= 1
        if ind[t] == 0:
            heapq.heappush(hq,t)
if len(ans) != n:
    print(-1)
else:
    print(*ans)
