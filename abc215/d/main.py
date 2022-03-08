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

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

n,m = LI()
A = LI()

checked = set()
ans = [True]*(m+1)
ans[0] = False

def check(x):
    global ans
    i = x
    while i <= m:
        ans[i] = False
        i += x

for a in A:
    s = prime_factorize(a)
    for x in s:
        if x in checked:
            continue
        check(x)
        checked.add(x)

print(sum(ans))
for i, an in enumerate(ans):
    if an:
        print(i)
