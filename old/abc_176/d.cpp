#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;
const int INF = 1001001001;
const int di[] = {0,-1,0,1};
const int dj[] = {-1,0,1,0};

int main() {
  int h, w, ch, cw, dh, dw;
  cin >> h >> w;
  cin >> ch >> cw >> dh >> dw;
  --ch; --cw; --dh; --dw;
  vector<string> s(h);
  rep(i,h) cin >> s[i];
  vector<vector<int>> dist(h, vector<int>(w,INF));
  deque<P> q;
  dist[ch][cw] = 0;
  q.emplace_back(ch, cw);
  while(!q.empty()){
    auto [i, j] = q.front();
    int d = dist[i][j];
    q.pop_front();
    rep(v,4){
      int ni = i+di[v], nj = j+dj[v];
      if(ni < 0 || ni >= h || nj < 0 || nj >= w) continue;
      if(s[ni][nj]=='#') continue;
      if(dist[ni][nj] <= d) continue;
      dist[ni][nj] = d;
      q.emplace_front(ni,nj);
    }
    for (int ei = -2; ei <= 2; ++ei) {
      for(int ej = -2; ej <= 2; ++ej){
        int ni = i+ei, nj=j+ej;
        if(ni < 0 || ni >= h || nj < 0 || nj >= w) continue;
        if(s[ni][nj]=='#') continue;
        if(dist[ni][nj] <= d+1) continue;
        dist[ni][nj] = d+1;
        q.emplace_back(ni,nj);
      }
    }
  }
  int ans = dist[dh][dw];
  if(ans == INF) ans = -1;
  cout << ans << endl;
  return 0;
}