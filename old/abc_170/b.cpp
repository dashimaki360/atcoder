#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;

int main() {
  int x, y;
  cin >> x >> y;
  int a = x*4 - y;
  string ans = "Yes";
  if(a<0) ans = "No";
  if(a&1) ans = "No";
  if(a > 2*x) ans = "No";
  cout << ans << endl;
  return 0;
}