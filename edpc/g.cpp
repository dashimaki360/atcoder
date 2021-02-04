#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;
void chmin(int& x, int y){x = min(x,y);}
void chmax(int& x, int y){x = max(x,y);}

vector<int> dp(100100);
vector<int> flag(100100);
vector<vector<int>> to(100100);
int f(int x){
  if(flag[x]) return dp[x];
  flag[x]=1;
  int fans=0;
  for(auto a: to[x]){
    fans = max(fans, f(a)+1);
  }
  return dp[x]=fans;
};

int main() {
  int n, m;
  cin >> n >> m;
  rep(i,m){
    int x, y;
    cin >> x >> y;
    --x; --y;
    to[x].push_back(y);
  }
  int ans=0;
  rep(i,n) chmax(ans, f(i));
  cout << ans << endl;
  return 0;
}