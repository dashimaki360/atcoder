#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;

const int N = 1000000007;

int main() {
  int h, w;
  cin >> h >> w;
  vector<string> s(h);
  rep(i,h) cin >> s[i];
  ll dp[h][w];
  ll dpr[h][w];
  ll dpd[h][w];
  ll dpv[h][w];
  rep(i,h)rep(j,w) dpr[i][j] = 0;
  rep(i,h)rep(j,w) dpd[i][j] = 0;
  rep(i,h)rep(j,w) dpv[i][j] = 0;
  dp[0][0] = 1;

  rep(i,h) rep(j,w){
    if(j!=0||i!=0 && s[i][j]!='#') 
      dp[i][j] =  (dpr[i][j] + dpd[i][j] + dpv[i][j])%N;
    if(j+1<w && s[i][j+1]!='#')
      dpr[i][j+1] = (dp[i][j] + dpr[i][j])%N;
    if(i+1<h && s[i+1][j]!='#')
       dpd[i+1][j] = (dp[i][j] + dpd[i][j])%N;
    if(j+1<w && i+1<h && s[i+1][j+1]!='#') 
      dpv[i+1][j+1] = (dp[i][j] + dpv[i][j])%N;
  }
  cout << dp[h-1][w-1] << endl;
  return 0;
}