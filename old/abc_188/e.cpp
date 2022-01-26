#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;
const int INF = 1001001001;

int main() {
  int n,m;
  cin >> n >> m;
  vector<int> a(n);
  rep(i, n) cin >> a[i];
  vector<int> mi(n, 2*INF);
  vector<vector<int>> road(n);
  rep(i, m){
    int x, y;
    cin >> x >> y;
    --x; --y;
    road[x].push_back(y);
  }
  int ans = -INF;
  rep(now, n){
    ans = max(ans, a[now] - mi[now]);
    mi[now] = min(a[now], mi[now]);
    for(auto x : road[now]){
      mi[x] = min(mi[now], mi[x]);
    }
  }
  cout << ans << endl;
  return 0;
}