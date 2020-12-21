#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;

int main() {
  ll n;
  cin >> n;
  ll a[n];
  rep(i,n) cin >> a[i];

  ll b = 0;
  ll c = 0;
  ll ans = 0;
  ll max_b = 0;

  rep(i,n){
    b += a[i];
    max_b = max(max_b, b);
    ans = max(ans, c + max_b);
    c = c + b;
  }
  cout << ans << endl;
  return 0;
}