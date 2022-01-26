import heapq
n, k = map(int, input().split())
p = list(map(int, input().split()))

que = p[0:k]
print(min(que))
heapq.heapify(que)
for i in range(k,n):
    # push or not
    minima = heapq.heappop(que)
    minima = max(minima, p[i])
    heapq.heappush(que, minima)
    # get ans
    ans = heapq.heappop(que)
    print(ans)
    heapq.heappush(que, ans)