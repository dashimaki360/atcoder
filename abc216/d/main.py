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
from collections import deque

n,m = LI()
to = [[] for _ in range(n)]
ins = [0]*n
q = deque()

for _ in range(m):
    k = I()
    A = LI()
    for i in range(k-1):
        to[A[i]-1].append(A[i+1]-1)
        ins[A[i+1]-1] += 1
for i in range(n):
     if ins[i] == 0:
         q.append(i)

# print(to, ins, q)

while len(q) > 0:
    x = q.popleft()
    for t in to[x]:
        ins[t] -= 1
        if ins[t] == 0:
            q.append(t)
if max(ins) > 0: no()
else: yes()
