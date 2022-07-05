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

n = I()
A = LI()
sumA = sum(A)
if sumA % 10:
    no()
    exit()
aim = sumA // 10
A = A+A
S = [0]*(2*n+1)
for i in range(2*n):
    S[i+1] = S[i] + A[i]

setS = set(S)

for s in S:
    x = aim + s
    if x in setS:
        yes()
        exit()

no()

