import heapq
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