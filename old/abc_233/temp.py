n, w = map(int, input().split())
cheeses = []
ans = 0
for i in range(n):
  a, b = map(int, input().split())
  cheeses.append([a,b])
  
cheeses.sort(reverse=True)
for cheese in cheeses:
  if w <= cheese[1]:
    ans += cheese[0] * w
    break
  else:
    ans += cheese[0] * cheese[1]
    w -= cheese[1]
print(ans)
