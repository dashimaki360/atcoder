#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;

int main() {
  int a, b;
  cin >> a >> b;
  int as = 0;
  int bs = 0;

  as += a/100;
  a = a%100;
  as += a/10;
  a = a%10;
  as += a;

  bs += b/100;
  b = b%100;
  bs += b/10;
  b = b%10;
  bs += b;
  cout << max(as, bs) << endl;
  return 0;
}