#!/usr/bin/env python3
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def yes(): print("Yes")
def no(): print("No")


def solve(n,k,A):
    ans = 0
    for i in range(n+1):
        for j in range(n+1-i):
            B = A[:i]
            if j != 0:
                B += A[-j:]
            B.sort()
            for l,b in enumerate(B):
                if l > k-i-j: break
                ans = max(ans, sum(B[l:]))
                # print(B[l:])
    print(ans)

n,k = LI()
A = LI()
solve(n,k,A)