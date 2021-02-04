#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;
void chmin(int& x, int y){x = min(x,y);}
void chmax(int& x, int y){x = max(x,y);}
const int N = 1000000007;

int main() {
  int h, w;
  cin >> h >> w;
  vector<string> m(h);
  rep(i,h) cin >> m[i];
  vector<vector<ll>> dp(h, vector<ll>(w,0));
  dp[0][0] = 1;
  rep(i,h) rep(j,w){
    if(i==0&&j==0) continue;
    if(m[i][j]=='#') continue;
    if(i-1>=0) dp[i][j] = (dp[i][j] + dp[i-1][j])%N;
    if(j-1>=0) dp[i][j] = (dp[i][j] + dp[i][j-1])%N;
    // cout << dp[i][j] << endl;
  }
  ll ans = dp[h-1][w-1];
  cout << ans << endl;
  return 0;
}