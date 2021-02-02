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
  vector<int> a(n), b(n), c(n);
  rep(i,n) cin >> a[i] >> b[i] >> c[i];
  vector<vector<int>> dp(n, vector<int>(3,0));
  // init day 1
  dp[0][0] = a[0];
  dp[0][1] = b[0];
  dp[0][2] = c[0];

  rep(i,n-1){
    chmax(dp[i+1][0], dp[i][1]+a[i+1]);
    chmax(dp[i+1][0], dp[i][2]+a[i+1]);

    chmax(dp[i+1][1], dp[i][0]+b[i+1]);
    chmax(dp[i+1][1], dp[i][2]+b[i+1]);

    chmax(dp[i+1][2], dp[i][1]+c[i+1]);
    chmax(dp[i+1][2], dp[i][0]+c[i+1]);
  }

  int ans = 0;
  rep(i,3){
    chmax(ans, dp[n-1][i]);
  }
  cout << ans << endl;
  return 0;
}