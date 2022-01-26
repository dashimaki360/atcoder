#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using p = pair<int,int>;

int main() {
  ll n, m, k;
  cin >> n >> m >> k;
  vector<int> a(n), b(m);
  rep(i,n) cin >. a[i];
  rep(i,m) cin >. b[i];

  ll t = 0;
  rep(i,m) t += b[i];

  int j = m;
  int ans = 0;
  rep(i, n+1) {
    while(j > 0 && t > k) {
      --j;
      t -= b[j];
    }
    if(t > k) break;
    ans = max(ans, i+j);
    if (i==n) break;
    t += a[i];
  }
  cout << ans << endl;
  return 0;
}