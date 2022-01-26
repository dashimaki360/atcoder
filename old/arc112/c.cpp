#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;
void chmin(int& x, int y){x = min(x,y);}
void chmax(int& x, int y){x = max(x,y);}

const int N = 100005;
vector<int> t(N);
vector<vector<int>> tt(N);
vector<int> s(N);
vector<int> dp(N, -1);

void add (int x){
  s[x]++;
  if(x!=1) add(t[x]);
  return;
};

ll func (int x){
  if(tt[x].empty()) return 1;
  for(int y: tt[x]){
    if(dp[y]==-1) func(y);
  }
}

int main() {
  int n;
  rep(i,n-1){
    int p;
    cin >> p;
    t[i+2] = p;
    add(p);
    tt[p].push_back(i+2);
  }
  ll ans = func(1);
  cout << ans << endl;

  return 0;
}