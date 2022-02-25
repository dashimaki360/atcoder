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
s = "B"*60
x = ("0"*60 + bin(n)[2:])[-60:]
q = ''
for a,b in zip(s,x):
    q += a
    q += b
q = q.replace('0','')
q = q.replace('1','A')
print(q)
