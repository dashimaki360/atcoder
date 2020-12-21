#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;

tuple<ll, ll, ll> extgcd(ll a, ll b) {
  if(b == 0) return {a,1,0};
  ll g, x, y;
  tie(g,x,y) = extgcd(b, a%b);
  return {g, y, x-a/b*y};
}

void solve(){
  int n, s, k;
  cin >> n >> s >> k;
  ll g, x, y;
  tie(g,x,y) = extgcd(k, n);
  if(s%g != 0){
    cout << -1 << endl;
    return;
  }
  n /= g;
  s /= g;
  k /= g;
  ll ans = ((x*-s)%n+n)%n;
  cout << ans << endl;
}

int main() {
  int t;
  cin >> t;
  rep(i,t) solve();
  return 0;
}