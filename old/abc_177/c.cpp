#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;
const ll N = 1000000007;

int main() {
  int n;
  cin >> n;
  vector<ll> a(n);
  rep(i,n) cin >> a[i];
  ll sum = 0;
  ll ans = 0;
  rep(i,n){
    ans += a[i] * sum;
    ans = ans%N;
    sum += a[i];
    sum = sum%N;
    // cout << i << j <<  a[i] << a[j] << endl;
  }
  cout << (ans%N+N)%N << endl;
  return 0;
}