#!/usr/bin/env python3
import sys, math
import collections
sys.setrecursionlimit(10**6)
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def yes(): print("Yes")
def no(): print("No")
MOD = 1000000007

# input tree
n = I()
path = [[] for _ in range(n)]
for i in range(n-1):
    a,b = LI()
    a -= 1
    b -= 1
    path[a].append([b,i])
    path[b].append([a,i])

que = collections.deque()
reach = [0]*n
que.append([0,-1])
reach[0] = 1
ans = [0] * (n-1)

while len(que):
    x, pa = que.popleft()
    color = 1
    for p, i in path[x]:
        if reach[p]: continue
        reach[p] = 1
        if color == pa: color += 1
        ans[i] = color
        que.append([p,color])
        color += 1

k = max(ans)
print(k)
for an in ans:
    print(an)
