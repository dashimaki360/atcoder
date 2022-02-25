#!/usr/bin/env python3
import sys, math
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def yes(): print("Yes")
def no(): print("No")
MOD = 1000000007

X = S()
n = I()
sl = [S() for _ in range(n)]

def comp(A):
    ret = 0
    for idx, a in enumerate(A):
        for i,x in enumerate(X):
            if a == x:
                ret += (27**(11-idx))*(i+1)
    return ret

sl.sort(key = comp)
for s in sl:
    # print(s, comp(s))
    print(s)


