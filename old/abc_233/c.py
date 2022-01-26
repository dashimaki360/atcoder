n, x = map(int, input().split())
A = []
l = []
ans = 0
for i in range(n):
    a = list(map(int, input().split()))
    A.append(a[1:])
    l.append(a[0])

def dfs(depth, sum):
    global ans
    # print(depth, sum)
    if depth == n:
        if sum == x:
            ans += 1
        return
    for i in range(l[depth]):
        dfs(depth+1, sum * A[depth][i])

dfs(0,1)
print(ans)
