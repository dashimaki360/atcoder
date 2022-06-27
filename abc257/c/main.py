#!/usr/bin/env python3
import sys, math ,heapq, bisect
from collections import deque
sys.setrecursionlimit(10**6)
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def yes(): print("Yes")
def no(): print("No")
MOD = 1000000007
INF = 10**18

n = I()
S = input()
W = LI()
# 座標圧縮
# 集合型にすることで重複を除去し、小さい順にソートする
C = sorted(set(W))
# B の各要素が何番目の要素なのかを辞書型で管理する
D = { v: i for i, v in enumerate(C) }
W = list(map(lambda v: D[v], W))

child = [0]*200005
adult = [0]*200005
num = 0
for i in range(n):
    if S[i] == '0':
        child[W[i]] += 1
    else:
        adult[W[i]] += 1
        num += 1

for i in range(1, len(child)):
    child[i] += child[i-1]
    adult[i] += adult[i-1]

ans = num
for i in range(len(child)):
    tmp = child[i]
    tmp += num - adult[i]
    ans = max(ans, tmp)
print(ans)

