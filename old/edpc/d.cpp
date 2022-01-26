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
  int n, W;
  cin >> n >> W;
  vector<int> v(n), w(n);
  rep(i,n) cin >> w[i] >> v[i];

  vector dp(n+1, vector<ll>(W+1, 0));
  // rep(i,W) {
  //   if(w[0]+i>=W) break;
  //   dp[0][w[0]+i] = v[0];
  // }

  rep(i,n+1) rep(j,W+1){
    if(i==0) continue;
    if(j-w[i-1]>=0) dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i-1]]+v[i-1]);
    else dp[i][j] = dp[i-1][j];
  }
  ll ans = dp[n][W];
  cout << ans << endl;

  return 0;
}