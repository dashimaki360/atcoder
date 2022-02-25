#!/usr/bin/env python3
import sys, math
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def yes(): print("Yes")
def no(): print("No")
MOD = 1000000007

def sosu(n):
  if n == 2:
    return True
  if n % 2 == 0:
    return False
  # nの平方根まで計算する
  m = math.floor(math.sqrt(n)) + 1
  for p in range(3, m, 2):
      if n % p == 0:
        return False
  return True

a,b,c,d = LI()
for i in range(a,b+1):
    for j in range(c, d+1):
        if sosu(i+j):
            break
    else:
        print("Takahashi")
        exit()
else:
    print("Aoki")
