# 座標圧縮
# 集合型にすることで重複を除去し、小さい順にソートする
C = sorted(set(A+B))
# B の各要素が何番目の要素なのかを辞書型で管理する
D = { v: i for i, v in enumerate(C) }
A = list(map(lambda v: D[v], A))
B = list(map(lambda v: D[v], B))