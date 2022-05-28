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

n,x,y = LI()
x -= 1
y -= 1
ans = [0]*n
for i in range(n):
    for j in range(i+1,n):
        d = min(abs(i-j), abs(i-x)+abs(j-y)+1, abs(j-x)+abs(i-y)+1)
        ans[d] += 1
for i in range(1,n):
    print(ans[i])
        
