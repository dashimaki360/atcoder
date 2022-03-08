#!/usr/bin/env python3
import sys, math
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def yes(): print("Yes")
def no(): print("No")
MOD = 1000000007
from collections import defaultdict, deque

def l_to_s(l):
    return "".join(map(str,l))

n = I()
A = [LI() for _ in range(n)]
P = LI()
pos = [9] * 9
for i in range(8):
    pos[P[i]-1] = i+1

root = [[] for _ in range(9)]
for u,v in A:
    root[u-1].append(v-1)
    root[v-1].append(u-1)
que = deque()
dist = defaultdict(int)
que.append(pos)
dist[l_to_s(pos)] = 0

while len(que) > 0:
    pos = que.popleft()
    zp = pos.index(9)
    d = dist[l_to_s(pos)]
    for r in root[zp]:
        npos = pos.copy()
        npos[zp] = pos[r]
        npos[r] = pos[zp]
        if not l_to_s(npos) in dist:
            dist[l_to_s(npos)] = d + 1
            que.append(npos)
    # print(l_to_s(pos), dist[l_to_s(pos)])

endp = "123456789"
if endp not in dist:
    ans = -1
else:
    ans = dist[endp]
print(ans)




