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
  vector<int> a(n), b(n);
  rep(i,n) cin >> a[i];
  rep(i,n) cin >> b[i];
  ll dot = 0;
  rep(i,n){
    dot += a[i] * b[i];
  }
  if(dot == 0){
    cout << "Yes" <<endl;
    return 0;
  }
  cout << "No" <<endl;

  return 0;
}