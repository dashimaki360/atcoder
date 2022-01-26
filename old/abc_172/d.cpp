#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;
using mint = 

int main() {
  int n;
  cin >> n;

  vector<ll> a(n+1);
  for(int i = 1; i <= n; i++){
    for(int j = 1; j*i<=n; j++){
      a[i*j] += 1;
    }
  }
  ll sum = 0;
  for(int i = 1; i <= n; i++){
    sum += ll(i)*a[i];
  }

  cout << sum << endl;

  return 0;
}