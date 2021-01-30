#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;
const int N = 1<<17;
const int M = 1<<17;
static int dp[M][N];

int main() {
  rep(i,1<<17) rep(j,N) dp[i][j] = 0;
  int n, m;
  cin >> n >> m;
  vector<vector<int>> ab(N);
  rep(i,m){
    int a, b;
    cin >> a >> b;
    --a; --b;
    ab[a].push_back(b);
    ab[b].push_back(a);
  }
  int K;
  cin >> K;
  ll sum = 0;
  rep(i,K){
    int c;
    cin >> c;
    c--;
    dp[1<<c][c] = 1;
    sum = sum|1<<c;
  }
  // cout << "sum " << sum << endl;

  for(auto x: ab){
    if(x.empty()){
      rep(i,K) x.push_back(i);
    }
  }

  rep(i,1<<K) rep(j,K) {
    if(dp[i][j]==0) continue;
    for(auto x: ab[j]){
      dp[i|1<<x][x] = min(dp[i][j]+1, dp[i|1<<x][x]);
    }
  }
  int ans = 1001001001;
  rep(j,N) {
    ans = min(dp[sum][j], ans);
  }
  cout << ans << endl;
  return 0;
}