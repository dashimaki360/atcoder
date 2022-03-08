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
import itertools

n,m,q = LI()
Q = [LI() for _ in range(q)]

it = itertools.combinations_with_replacement(list(range(1,m+1)),n)
ans = 0
for A in it:
    tmp = 0
    for a,b,c,d in Q:
        a -= 1
        b -= 1
        if A[b] - A[a] == c:
            tmp += d
    ans = max(ans, tmp)
print(ans)
