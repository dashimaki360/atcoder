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

n,k = LI()
A = LI()
idx = 0
tmp = [-1] * n
tmp[0] = 0
for i in range(1,1001001001):
    idx += A[idx%n]
    if i == k:
        print(idx)
        exit()
    if tmp[idx%n] >= 0:
        loop = i - tmp[idx%n]
        k = (k - i)%loop + i
    tmp[idx%n] = i







