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
  ll n;
  cin >> n;
  ll ans = 0;
  if(n >= 1000) ans += n-1000+1;
  if(n >= 1000000) ans += n-1000000+1;
  if(n >= 1000000000) ans += n-1000000000+1;
  if(n >= 1000000000000) ans += n-1000000000000+1;
  if(n >= 1000000000000000) ans += n-1000000000000000+1;
  cout << ans << endl;


  return 0;
}