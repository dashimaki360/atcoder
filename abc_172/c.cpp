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
  vector<ll> asum(n+1), bsum(m+1);
  rep(i,n){
    ll a;
    cin >> a;
    asum[i+1] = asum[i] + a;
  }
  rep(i,m) {
    ll b;
    cin >> b;
    bsum[i+1] = bsum[i] + b;
  }

  ll t = n;
  rep(i,n) {
    if(asum[i+1] > k) {
      t = i;
      break;
    }
  }
  // cout << "t: " << t << endl;
  // rep(i,n) cout <<"a: " << asum[i] << endl;

  ll ans = t;
  ll s = 0;
  rep(i,t+1){
    ll p = k - asum[t-i];
    while(s <= m && p >= bsum[s]){
      s++;
    }
    ans = max(ans, t-i + s-1);
  }
  cout << ans << endl;
  return 0;
}