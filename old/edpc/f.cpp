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
  string s, t;
  cin >> s >> t;
  int slen = s.size();
  int tlen = t.size();
  vector dp(slen+1, vector<int>(tlen+1, 0));
  rep(i, slen+1) rep(j, tlen+1){
    if(i==0 || j==0) continue;
    if(s[i-1]==t[j-1]) dp[i][j] = dp[i-1][j-1] + 1;
    else dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
    // cout << dp[i][j] << endl;
  }
  int len = dp[slen][tlen];
  // cout << len << endl;
  if(len == 0) {
    cout << "" << endl;
    return 0;
  }
  string ans(len, '0');
  int i = slen;
  int j = tlen;
  while(len > 0){
    if(s[i-1]==t[j-1]){
    // cout << "LINE: " << __LINE__ << endl;
      ans[len-1] = s[i-1];
      i--; j--; len--;
    }else if(dp[i][j] == dp[i-1][j]){
    // cout << "LINE: " << __LINE__ << endl;
      i--;
    }else {
    // cout << "LINE: " << __LINE__ << endl;
      j--;
    }
  }
  cout << ans << endl;
  return 0;
}