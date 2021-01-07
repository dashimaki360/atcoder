#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;

int main() {
  ll a;
  float b;
  cin >> a >> b;
  cout << (a*ll(b*100+0.1))/100 << endl;
  return 0;
}