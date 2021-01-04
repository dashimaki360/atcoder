#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;

int main() {
  int n;
  cin >> n;
  vector<ll> a(n), b(n), a2b(n);
  ll sum_b = 0;
  rep(i,n) {
    // cin >> a[i] >> b[i];
    cin >> b[i] >> a[i];
    a2b[i] = a[i] + 2*b[i];
    sum_b += b[i];
  }
  sort(a2b.begin(), a2b.end(), greater<ll>());
  rep(i,n){
    sum_b -= a2b[i];
    if(sum_b<0){
      cout << i+1 << endl;
      return 0;
    }
  }
  return 0;
}