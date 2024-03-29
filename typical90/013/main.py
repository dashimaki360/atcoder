#!/usr/bin/env python3
import sys, math ,heapq, bisect
from collections import deque
sys.setrecursionlimit(10**6)
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def yes(): print("Yes")
def no(): print("No")
MOD = 998244353
INF = 10**18

n,m = LI()
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = LI()
    graph[a-1].append([b-1, c])
    graph[b-1].append([a-1, c])  # 有向グラフなら消す

def dijkstra(edges, num_node, st_node):
    node = [float('inf')] * num_node    #スタート地点以外の値は∞で初期化
    node[st_node] = 0     #スタートは0で初期化

    node_name = []
    heapq.heappush(node_name, [0, st_node])

    while len(node_name) > 0:
        #ヒープから取り出し
        _, min_point = heapq.heappop(node_name)

        #経路の要素を各変数に格納することで，視覚的に見やすくする
        for factor in edges[min_point]:
            goal = factor[0]   #終点
            cost  = factor[1]   #コスト

            #更新条件
            if node[min_point] + cost < node[goal]:
                node[goal] = node[min_point] + cost     #更新
                #ヒープに登録
                heapq.heappush(node_name, [node[min_point] + cost, goal])
    return node

d1 = dijkstra(graph, n, 0)
d2 = dijkstra(graph, n, n-1)
for i in range(n):
    print(d1[i]+d2[i])

