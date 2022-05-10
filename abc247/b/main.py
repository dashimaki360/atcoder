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
MOD = 1000000007
INF = 10**18

n = I()
A = []
B = []

for i in range(n):
    a, b = input().split()
    A.append(a)
    B.append(b)
for i in range(n):
    aout = False
    bout = False
    for j in range(n):
        if i == j: continue
        if A[i] == A[j] or A[i] == B[j]:
            aout = True
        if B[i] == A[j] or B[i] == B[j]:
            bout = True
    if aout and bout:
        no()
        exit()
yes()