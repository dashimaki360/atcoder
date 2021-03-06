#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;
void chmin(int& x, int y){x = min(x,y);}
void chmax(int& x, int y){x = max(x,y);}

int main() {
  int n;
  cin >> n;
  double ans = 0;
  rep(i,n){
    ans += double(1.0)/((double)i+1);
  }
  ans *= double(n);
  ans -= double(1);
  printf("%.15f\n", ans);
  return 0;
}