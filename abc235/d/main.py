#!/usr/bin/env python3
import sys, math
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def yes(): print("Yes")
def no(): print("No")
MOD = 1000000007
from collections import deque

a,n = LI()

memo = [-1]*1000005
que = deque()
que.append([1,0])
memo[1] = 0

while len(que) > 0:
    node = que.popleft()
    k = node[1]
    node = node[0]

    x = node*a
    if x <= 1000000 and memo[x] == -1:
        que.append([x,k+1])
        memo[x] = k+1
    
    if node%10 != 0 and node > 10:
        x = int(str(node)[-1] + str(node)[:-1])
        if x <= 1000000 and memo[x] == -1:
            que.append([x,k+1])
            memo[x] = k+1
ans = memo[n]
print(ans)
