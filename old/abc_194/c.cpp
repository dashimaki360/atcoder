#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;
void chmin(int& x, int y){x = min(x,y);}
void chmax(int& x, int y){x = max(x,y);}

int main() {
  int n;
  cin >> n;
  vector<ll> a(410,0);
  rep(i,n) {
    ll x;
    cin >> x;
    x += 202;
    a[x] += 1;
  }
  ll ans = 0;
  rep(i, 410) rep(j,i){
    if(i==j) continue;
    ans += (ll)(i-j) * (ll)(i-j) * a[i] * a[j];
  }
  cout << ans << endl;
  return 0;
}