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


from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

def solve_uf():
    n = I()
    X = LI()
    for i in range(n):
        X[i] -= 1
    C = LI()
    uf = UnionFind(n)
    ans = 0
    for i,x in enumerate(X):
        if uf.find(i) != uf.find(x):
            uf.union(i,x)
        else:
            min_cost = C[i]
            to = X[i]
            while to != i:
                min_cost = min(min_cost, C[to])
                to = X[to]
            ans += min_cost
    print(ans)


# 強連結成分分解(SCC): グラフGに対するSCCを行う
# 入力: <N>: 頂点サイズ, <G>: 順方向の有向グラフ, <RG>: 逆方向の有向グラフ
# 出力: (<ラベル数>, <各頂点のラベル番号>)
def scc(N, G, RG):
    order = []
    used = [0]*N
    group = [None]*N
    def dfs(s):
        used[s] = 1
        for t in G[s]:
            if not used[t]:
                dfs(t)
        order.append(s)
    def rdfs(s, col):
        group[s] = col
        used[s] = 1
        for t in RG[s]:
            if not used[t]:
                rdfs(t, col)
    for i in range(N):
        if not used[i]:
            dfs(i)
    used = [0]*N
    label = 0
    for s in reversed(order):
        if not used[s]:
            rdfs(s, label)
            label += 1
    return label, group

def solve_scc():
    n = I()
    X = LI()
    C = LI()
    graph = [[] for _ in range(n)]
    rgraph = [[] for _ in range(n)]
    for i in range(n):
        graph[i].append(X[i]-1)
        rgraph[X[i]-1].append(i)  # 有向グラフなら消す
    num, label = scc(n,graph, rgraph)
    group = [[] for _ in range(num)]
    for i in range(n):
        group[label[i]].append(i)
    ans = 0
    for nodes in group:
        if len(nodes) <= 1:
            continue
        minc = INF
        for node in nodes:
            minc = min(minc, C[node])
        ans += minc
    print(ans)
        





    
    

solve_scc()
