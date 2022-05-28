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

S = input()
A = []
is_r = False
for s in S:
    if s=="R" and is_r:
        A[-1] += 1
    elif s=="L" and not is_r:
        A[-1] += 1
    else:
        is_r = not is_r
        A.append(1)

ans = [0]*len(S)
idx = -1
for i,a in enumerate(A):
    if i%2 == 0:
        idx += a
        ans[idx] += a - a//2
        ans[idx+1] += a//2
    else:
        ans[idx+1] += a - a//2
        ans[idx] += a//2
        idx += a
# print(A)
print(*ans)


