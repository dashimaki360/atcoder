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

def is_prime(x):
    for i in range(2,int(x**0.5)):
        if x%i == 0:
            return False
    else:
        return True

n = I()
for i in range(n,1001001001):
    if is_prime(i):
        print(i)
        break