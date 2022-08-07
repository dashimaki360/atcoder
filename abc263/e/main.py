#!/usr/bin/env python3
import sys, math ,heapq, bisect
from collections import deque
sys.setrecursionlimit(10**6)
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def yes(): print("Yes")
def no(): print("No")
MOD = 998244353
INF = 10**18

class Fenwick_Tree:
    def __init__(self, n):
        self._n = n
        self.data = [0] * n

    def add(self, p, x):
        assert 0 <= p < self._n
        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p

    def sum(self, l, r):
        assert 0 <= l <= r <= self._n
        return self._sum(r) - self._sum(l)

    def _sum(self, r):
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r
        return s


# USE SAMPLE
    # n = 8 
    # a = [0, 1, 2, 3, 4, 5, 6, 7]
    # fw = Fenwick_Tree(n)
    # for i, a_i in enumerate(a): fw.add(i, a_i)  # 数列aで初期化
    # print(fw.sum(2, 4))  # 5
    # print(fw.sum(6, 7))  # 6 sum(i, i + 1)でa[i]が得られる
    # fw.add(2, 6)  # a[2] += 6
    # a[2] += 6
    # fw.add(5, -1)  # a[5] += -1
    # a[5] += -1
    # print(a)  # [0, 1, 8, 3, 4, 4, 6, 7]
    # print(fw.sum(0, 3))  # 9
    # print(fw.sum(3, 7))  # 17


n = I()
A = LI()
dp = Fenwick_Tree(n)

for i in range(n-2, -1, -1):
    a = A[i]
    tmp = dp.sum(i+1, i+a+1)
    tmp *= pow(a, MOD-2, MOD)
    tmp += 1
    tmp += pow(a, MOD-2, MOD)
    tmp %= MOD
    dp.add(i, tmp) 
print(dp.sum(0,1))
