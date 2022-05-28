# https://atcoder.jp/contests/abc130/tasks/abc130_d
n, k = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
r = 0
p = 0
for l in range(n):
    while r < n and p + A[r] < k: # 1個進めたときに条件を満たすか
        p += A[r]
        r += 1
    # l,r は条件を満たしているかrが終端
    ans += n - r
    if l == r:
        r += 1
    else:
        p -= A[l]

# int right = 0;     
# for (int left = 0; left < n; ++left) {
#     while (right < n && (right を 1 個進めたときに条件を満たす)) {
#         /* 実際に right を 1 進める */
#         // ex: sum += a[right];
#         ++right;
#     }

#     /* break した状態で right は条件を満たす最大なので、何かする */
#     // ex: res += (right - left);

#     /* left をインクリメントする準備 */
#     // ex: if (right == left) ++right;
#     // ex: else sum -= a[left];
# }