#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;
const int N = 998244353;

int main() {
  ll n, k;
  cin >> n >> k;
  vector<P> r(k);
  rep(i,k) {
    int x, y;
    cin >> x >> y;
    r[i].first = x;
    r[i].second = y;
  }
  sort(r.begin(), r.end());
  ll dp[n+1];
  ll dpsum[n+1];
  rep(i,n+1) dp[i] = 0;
  rep(i,n+1) dpsum[i] = 0;
  dp[0] = 0;
  dp[1] = 1;
  dpsum[0] = 0;
  dpsum[1] = 1;

  rep(i, n){
    if(i==0) continue;
    for(auto lr: r){
      if(lr.first > i) break;
      int st = lr.first;
      int ed = lr.second;
      if(lr.second > i){
        ed = i;
      } 
      // cout << "ST,ED: " << st << ", " << ed << endl;
      dp[i+1] += dpsum[i-st+1] - dpsum[i-ed];
      dp[i+1] %= N;
    }
    dpsum[i+1] = dpsum[i] + dp[i+1];
    dpsum[i+1] %= N;
  }
  // cout << " final values " << endl;
  // rep(i,n+1) cout << i << ", " << dp[i] << ", " << dpsum[i] <<endl;
  cout << (dp[n]%N + N)%N << endl;
  return 0;
}