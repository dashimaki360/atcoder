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

s = input()
q = I()
TK = [LI() for _ in range(q)]

A = [-1] * len(s)
for i in range(len(s)):
    if s[i] == "A":
        A[i] = 0
    elif s[i] == "B":
        A[i] = 1
    elif s[i] == "C":
        A[i] = 2

for t, k in TK:
    k = k-1
    ans = 0
    ans += t%3
    for i in range(t):
        ans += k%2
        k //=2
        if k == 0:
            break
    ans += A[k]
    ans %= 3
        
    if ans == 0:
        print("A")
    elif ans == 1:
        print("B")
    else:
        print("C")



