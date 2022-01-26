#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;

int main() {
  int h, w, k;
  cin >> h >> w >> k;
  vector<string> gg(h), g(h);
  rep(i,h) cin >> gg[i];

  int ans = 0;
  rep(i,1<<h) rep(j,1<<w){
    rep(i,h) rep(j,w) g[i][j] = gg[i][j];
    rep(ii,h){
      if(i>>ii&1){
        rep(p,w) g[ii][p]='.';
      }
    }
    rep(jj,w){
      if(j>>jj&1){
        rep(p,h) g[p][jj]='.';
      }
    }

    int sum = 0;
    rep(ii,h) rep(jj,w){
      if(g[ii][jj]=='#') sum++;
    }
    if(sum==k){
      ans++;
    }
    // cout << i << " " << j << " " << sum << endl;
  }
  cout << ans << endl;


  return 0;
}