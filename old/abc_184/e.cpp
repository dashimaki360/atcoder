#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;

void chmin(int& x, int y){x = min(x,y);}
const int INF = 1001001001;
const int di[] = {0,1,0,-1};
const int dj[] = {1,0,-1,0};

int main() {
  int h, w;
  cin >> h >> w;
  vector<string> s(h);
  rep(i,h) cin >> s[i];
  vector dist(h, vector(w, INF));
  queue<P> q;
  rep(i,h)rep(j,w) {
    if(s[i][j] == 'S'){
      q.emplace(i,j);
      dist[i][j] = 0;
    }
  }
  vector<vector<P>> warps(256);
  rep(i,h)rep(j,w) warps[s[i][j]].emplace_back(i,j);

  while(!q.empty()) {
    auto [i,j] = q.front();
    q.pop();

    //check goal
    if(s[i][j] == 'G'){
      cout << dist[i][j] << endl;
      return 0;
    }

    // AWSD move
    rep(v,4){
      int ni = i+di[v], nj = j+dj[v];
      if(ni < 0 || nj < 0) continue;
      if(ni >= h || nj >= w) continue;
      if(s[ni][nj]=='#') continue;
      if(dist[ni][nj] != INF) continue;
      dist[ni][nj] = dist[i][j]+1;
      q.emplace(ni, nj);
    }

    //WARP move
    if(islower(s[i][j])) {
      for (P p: warps[s[i][j]]){
        int ni = p.first, nj = p.second;
        if(dist[ni][nj] != INF) continue;
        dist[ni][nj] = dist[i][j]+1;
        q.emplace(ni, nj);
      }
      warps[s[i][j]] = vector<P>();
    }

  }
  cout << -1 << endl;
  return 0;
}