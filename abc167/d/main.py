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

n,K = LI()
A = LI()
s = []
ord = [-1] * (n+1)

c = 1
l = 0
v = 1
while ord[v] == -1:
    ord[v] = len(s)
    s.append(v)
    v = A[v-1]
c = len(s) - ord[v]
l = ord[v]

if K < l:
    print(s[K])
else:
    K -= l
    K %= c
    print(s[l+K])

# for i in range(n):
#     A[i] -= 1
# logk = 1
# while (1<<logk) <= K:
#     logk += 1

# doubling = [[0]*n for _ in range(logk)]
# for i in range(n):
#     doubling[0][i] = A[i]

# for k in range(logk-1):
#     for i in range(n):
#         doubling[k+1][i] = doubling[k][doubling[k][i]]

# ans = 0
# i = 0
# while K > 0:
#     if K&1:
#         ans = doubling[i][ans]
#     K = K >> 1
#     i += 1
# print(ans+1)

