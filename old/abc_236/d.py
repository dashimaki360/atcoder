import itertools
n = int(input())
nn = n*2
A = []
for i in range(nn - 1):
    A.append(list(map(int, input().split())))

print(A[1][0])

ans = 0
def dfs(p, x):
    global ans
    if p == 0:
        # print(ans, x)
        ans = max(ans, x)
        return
    q = []
    for i in range(nn):
        if p>>i & 1:
             q.append(i)
    # print(q, x)
    comb = itertools.combinations(q,2)
    for v in comb:
        a = v[0]
        b = v[1] - v[0] - 1
        xx = A[a][b]
        p = p^(1<<v[0])^(1<<v[1])
        dfs(p,x^xx)


dfs((1<<nn) -1, 0)
print(ans)