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

k = I()

A = []
def dfs(x):
    global A
    if x > 10**10:
        return
    A.append(x)
    
    a = x%10
    if a - 1 >= 0:
        dfs(x*10+a-1)
    if a+1 <= 9:
        dfs(x*10+a+1)
    dfs(x*10+a)


for i in range(1,10):
    dfs(i)
A.sort()
print(A[k-1])


