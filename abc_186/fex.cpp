#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;


int main() {
  int h, w, n;
  cin >> h >> w >> n;
  vector<int> a(w,h), b(h,w);
  rep(i,n) {
    int x, y;
    cin >> x >> y;
    --x; --y;
    a[y] = min(a[y], x);
    b[x] = min(b[x], y);
  }
  ll ans = 0;
  rep(y,b[0]) ans += a[y];
  rep(x,a[0]) ans += b[x];
  // fenwick_tree<int> t(w);
  // rep(y,b[0]) t.add(y,1);
  vector<int> t(w);
  rep(y,b[0]) ++t[y];
  vector<vector<int>> ends(h+1);
  rep(y,b[0]) ends[a[y]].push_back(y);
  rep(x,a[0]){
    // for(int y : ends[x]) t.add(y, -1);
    // ans -= t.sum(0, b[x]);
    for(int y : ends[x]) --t[y];
    rep(i,b[x]) ans -= t[i];
  }
  cout << ans << endl;

  return 0;
}