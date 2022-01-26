#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;

int main() {
  int H, W, M;
  cin >> H >> W >> M;
  // vector<int> h(M), w(M);
  vector<int> cnth(H), cntw(W);
  set<P> s;
  rep(i, M){
    int a, b;
    cin >> a >> b;
    --a; --b;
    // h[i]=a; w[i]=b;
    cnth[a] += 1; cntw[b] += 1;
    s.emplace(a,b);
  }

  int maxh=0, maxw=0;
  rep(i,H) maxh = max(maxh, cnth[i]);
  rep(i,W) maxw = max(maxw, cntw[i]);
  vector<int> maxh_idxs, maxw_idxs;
  rep(i,H){
    if(maxh==cnth[i]) maxh_idxs.push_back(i);
  }
  rep(i,W){
    if(maxw==cntw[i]) maxw_idxs.push_back(i);
  }

  bool flag = false;
  for(auto x : maxh_idxs){
    for(auto y : maxw_idxs){
      if(s.count(P(x,y))) continue;
      cout << maxw + maxh << endl;
      return 0;
    }
  }
  cout << maxw + maxh -1 << endl;
  return 0;
}