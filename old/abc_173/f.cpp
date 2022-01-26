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
  ll sum = 0;
  for (int i = 1; i <= n; i++) {
    // sum += i*(n-i+1);
    sum += (ll(i)*(i+1))/2;
  }

  rep(i, n-1){
    ll a, b;
    cin >> a >> b;
    if(a > b) swap(a, b);
    sum -= a * (n-b+1);
  }
  cout << sum << endl;

  return 0;
}
