#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;
void chmin(int& x, int y){x = min(x,y);}
void chmax(int& x, int y){x = max(x,y);}
const int INF = 1001001001;

int main() {
  int n;
  cin >> n;
  vector<int> a(n);
  rep(i,n) cin >> a[i];
  vector<int> dp(n, INF);
  dp[0] = 0;
  rep(i,n){
    if(i+1 >= n) continue;
    chmin(dp[i+1], dp[i] + abs(a[i]-a[i+1]));
    if(i+2 >= n) continue;
    chmin(dp[i+2], dp[i] + abs(a[i]-a[i+2]));
  }
  int ans = dp[n-1];
  cout << ans << endl;
  return 0;
}