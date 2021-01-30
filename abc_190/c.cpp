#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;

int main() {
  int n, m;
  cin >> n >> m;
  vector<int> a(m), b(m);
  rep(i,m) cin >> a[i] >> b[i];
  int k;
  cin >> k;
  // cout << "k" << k << endl;
  vector<int> c(k), d(k);
  rep(i,k) cin >> c[i] >> d[i];
  int ans = 0;
  rep(i, 1<<k){
    vector<int> bar(n+1);
    int temp = 0;
    rep(j,k){
      if(i>>j&1) bar[c[j]] = 1;
      else bar[d[j]] = 1;
    }
    rep(j,m){
      if(bar[a[j]]==1&&bar[b[j]]==1) temp++;
    }
    ans = max(ans, temp);
  }
  cout << ans << endl;
  return 0;
}