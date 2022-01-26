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
  int n, m;
  cin >> n >> m;
  vector<vector<int>> road(n);
  rep(i,m){
    int a, b;
    cin >> a >> b;
    --a; --b;
    road[a].push_back(b);
    road[b].push_back(a);
  }
  int k;
  cin >> k;
  vector<int> c(k);
  rep(i,k) {
    cin >> c[i];
    --c[i];
  }

  const int INF = 1001001001;
  auto bfs = [&](int sv) {
    vector<int> d(n, INF);
    queue<int> q;
    d[sv] = 0;
    q.push(sv);
    while (!q.empty()){
      int v = q.front(); q.pop();
      for(int u: road[v]){
        if(d[u] != INF) continue;
        d[u] = d[v]+1;
        q.push(u);
      }
    }
    return d;
  };

  vector<vector<int>> dist(k, vector<int>(k));
  rep(i,k){
    // transrate n index > k index
    vector<int> d = bfs(c[i]);
    rep(j,k) dist[i][j] = d[c[j]];
  }

  ll k2 = 1<<k;
  vector dp(k2, vector<int>(k, INF));
  rep(i,k) dp[1<<i][i] = 1;
  rep(i, k2) rep(j,k){
    if(~i>>j&1) continue;
    rep(x,k){
      if(i>>x&1) continue;
      chmin(dp[i|1<<x][x], dp[i][j] + dist[j][x]);
    }
  }

  int ans = INF;
  rep(i,k){
    chmin(ans, dp[k2-1][i]);
  }
  if(ans == INF) ans = -1;
  cout << ans << endl;
  return 0;
}