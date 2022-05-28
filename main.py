n,m = map(int, input().split())
A = list(map(int, input().split()))
B = []
for i in range(m):
    b,c = map(int, input().split())
    B.append([c,b])
B.sort(reverse=True)
cnt = 0
for c,b in B:
    A += [c]*b
    cnt += b
    if cnt > n:
        break
A.sort(reverse=True)
ans = sum(A[:n])
print(ans)


    