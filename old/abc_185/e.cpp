#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;
void chmin(int& x, int y){x = min(x,y);}
const int INF = 1001001001;

int main() {
  int n, m;
  cin >> n >> m;
  vector<int> a(n), b(m);
  rep(i, n) cin >> a[i];
  rep(i, m) cin >> b[i];
  int dp[n+1][m+1];
  rep(i,n+1) rep(j,m+1) dp[i][j] = INF;
  dp[0][0] = 0;
  rep(i,n+1) rep(j,m+1){
    if(i+1 <= n) chmin(dp[i+1][j], dp[i][j]+1);
    if(j+1 <= m) chmin(dp[i][j+1], dp[i][j]+1);
    if(i+1 <=n && j+1<=m){
    if(a[i] == b[j]){
        chmin(dp[i+1][j+1], dp[i][j]);
      }else{
        chmin(dp[i+1][j+1], dp[i][j]+1);
      }
    }
  }
  cout << dp[n][m] << endl;
  return 0;
}