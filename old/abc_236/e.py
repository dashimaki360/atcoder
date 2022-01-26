n = int(input())
nn = n*2
A = []
for i in range(nn - 1):
    A.append(list(map(int, input().split())))
used = [False] * (2*n)
ans = 0

def dfs(i, tot):
    if i == n:
        global ans
        ans = max(ans, tot)
        return

    for j in range(2*n):
        if not used[j]:
            used[j] = True
            break
    for k in range(j + 1, 2*n):
        if not used[k]:
            used[k] = True
            dfs(i + 1, tot ^ A[j][k - j - 1])
            used[k] = False
    used[j] = False

dfs(0, 0)
print(ans)