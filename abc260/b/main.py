#!/usr/bin/env python3
from re import M
import sys, math ,heapq, bisect
from collections import deque
sys.setrecursionlimit(10**6)
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def yes(): print("Yes")
def no(): print("No")
MOD = 1000000007
INF = 10**18

n,x,y,z = LI()
A = LI()
B = LI()
C = []

for i,[a,b] in enumerate(zip(A,B)):
    tmp = a*1005*1005 + b*1005 + a+b
    C.append([tmp,i+1])

C.sort()
ans = []
for c,idx in C[:(x+y+z)]:
    ans.append(idx)
ans.sort()
for an in ans:
    print(an)

