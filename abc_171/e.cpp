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
  vector<int> a(n);
  rep(i,n) cin >> a[i];
  ll sum = 0;
  rep(i,n){
    sum ^= a[i];
  }
  rep(i,n){
    int ans = sum ^ a[i];
    cout << ans << " ";
  }
  return 0;
}