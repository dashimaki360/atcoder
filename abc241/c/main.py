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
S1 = [S() for _ in range(n)]


for s in S1:
    for i in range(n-5):
        if 4 <= s[i:i+6].count('#'):
            yes()
            exit()

S2 = ["".join(x) for x in zip(*S1)]
for s in S2:
    for i in range(n-5):
        if 4 <= s[i:i+6].count('#'):
            yes()
            exit()

for i in range(n-5):
    for j in range(n-5):
        S3 = ""
        S4 = ""
        for x in range(6):
            S3 += S1[i+x][j+x]
            S4 += S1[i+x][j+5-x]
        if 4 <= S3.count('#'):
            yes()
            exit()
        if 4 <= S4.count('#'):
            yes()
            exit()

no()
