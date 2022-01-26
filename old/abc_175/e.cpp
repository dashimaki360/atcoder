#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;
void chmax(ll& x, ll y){x=max(x,y);}

ll dp[3005][3005][4];
ll value[3005][3005];

int main() {
  int r, c, K;
  cin >> r >> c >> K;
  rep(i,r) rep(j,c) rep(k, 4){
    dp[i][j][k] = 0;
  }
  rep(i,r) rep(j,c) value[i][j] = 0; 
  rep(i,K){
    ll x, y, v;
    cin >> x >> y >> v;
    x--; y--;
    value[x][y] = v;
  }
  dp[0][0][0] = 0;
  dp[0][0][1] = value[0][0];

  rep(i,r) rep(j,c){
    chmax(dp[i][j+1][0], dp[i][j][0]);
    chmax(dp[i][j+1][1], max(dp[i][j][1], dp[i][j][0] + value[i][j+1]) );
    chmax(dp[i][j+1][2], max(dp[i][j][2], dp[i][j][1] + value[i][j+1]));
    chmax(dp[i][j+1][3], max(dp[i][j][3], dp[i][j][2] + value[i][j+1]));

    chmax(dp[i+1][j][0], max(max(dp[i][j][0], dp[i][j][1]), max(dp[i][j][2], dp[i][j][3])) );
    chmax(dp[i+1][j][1], max(max(dp[i][j][0], dp[i][j][1]), max(dp[i][j][2], dp[i][j][3])) + value[i+1][j]);
    // dp[i+1][j][2] = 0;
  }
  ll ans = dp[r-1][c-1][0];
  ans = max(ans, dp[r-1][c-1][1]);
  ans = max(ans, dp[r-1][c-1][2]);
  ans = max(ans, dp[r-1][c-1][3]);
  cout << ans << endl;
  //debug
  // rep(k, 4){
  //   rep(i,r){
  //     rep(j,c){
  //         cout << dp[i][j][k] << " " ;
  //     }
  //     cout << endl;
  //   } 
  // }
  return 0;
}