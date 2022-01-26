#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;

int main() {
  ll x, y, a, b;
  cin >> x >> y >> a >> b;
  ll exp=0;
  while ((double)x*a <= 2e18 && a*x<=x+b && a*x<y) {
      x *= a;
      exp++;
  }
  exp += (y-x-1)/b;
  cout << exp << endl;
  return 0;
}