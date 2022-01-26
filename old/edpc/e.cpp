#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;
void chmin(int& x, int y){x = min(x,y);}
void chmax(int& x, int y){x = max(x,y);}
const ll INF = 100100101001001;

int main() {
  int n, W;
  cin >> n >> W;
  vector<int> v(n+1), w(n+1);
  rep(i,n) cin >> w[i+1] >> v[i+1];

  const int M = 100005;
  vector dp(n+1, vector<ll>(M+1, INF));
  dp[0][0] = 0;
  rep(i, n+1) rep(j, M+1){
    if(i-1 < 0) continue;
    if(j-v[i] >= 0) dp[i][j] = min(dp[i-1][j], dp[i-1][j-v[i]] + w[i]);
    else dp[i][j] = dp[i-1][j];
  }
  int i=M;
  while(1){
    if(i<=0) break;
    if(dp[n][i] <= W) break;
    i--;
  }
  int ans = i;
  cout << ans << endl;
  return 0;
}