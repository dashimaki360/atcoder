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
  vector<ll> a(n);
  rep(i,n) cin >> a[i];

  ll sum = 0;
  sort(a.begin(), a.end());
  
  for (int i = 0; i < n; i++) {
    sum += a[i]*(2*i-n+1);
  }
  cout << sum << endl;
  return 0;
}