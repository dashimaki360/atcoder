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



n = I()
A = LI()
cnt = [0]*200
d = min(n,8)

def func(x):
    B = []
    for j in range(d):
        if x>>j&1:
            B.append(j+1)
    B = [len(B)] + B
    print(*B)

for i in range(1<<d):
    sum = 0
    for j in range(d):
        if i>>j&1:
            sum += A[j]
    if cnt[sum%200]:
        yes()
        func(cnt[sum%200])
        func(i)
        exit()
    else:
        cnt[sum%200] = i
no()
