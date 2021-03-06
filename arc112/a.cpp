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
  rep(i,n){
    int l, r;
    cin >> l >> r;
    if(r-2*l < 0){
      ll ans = 0;
      cout << ans << endl;
      continue;
    }
    ll m = r-2*l+1;
    ll ans = ((r+2*l)*m)/2 + (-2*l+1)*m;
    cout << ans << endl;
  }
  return 0;
}