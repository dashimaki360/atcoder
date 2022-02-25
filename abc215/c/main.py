#!/usr/bin/env python3
import sys, math
import itertools
sys.setrecursionlimit(10**6)
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def yes(): print("Yes")
def no(): print("No")
MOD = 1000000007

s, k= LS()
k = int(k)
t = set(itertools.permutations(s))
t = sorted(t)
print("".join(t[k - 1]))