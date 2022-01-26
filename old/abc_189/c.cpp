#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;
const int INF = 1001001001;

int main() {
  int n;
  cin >> n;
  vector<ll> a(n);
  rep(i,n) cin >> a[i];
  ll ans = 0;
  ll mi = INF;
  for(ll i=0; i < n; i++){
    mi = INF;
    for(ll j=i; j < n; j++){
      mi = min(mi, a[j]);
      ans = max(ans, mi*(j-i+1) );
    }
  }
  cout << ans << endl;
  return 0;
}