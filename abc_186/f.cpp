#include <bits/stdc++.h>
using namespace std;
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int,int>;


int main() {
  int h, w, m;
  cin >> h >> w >> m;
  bool up[h][w] = {false};
  bool side[h][w] = {false};

  vector<int> x(m), y(m);
  rep(i,m){
    int a, b;
    cin >> a >> b;
    x[i] = a-1;
    y[i] = b-1;
    if(a-1==0){
      rep(j,w){
        if(y[i]+j+1 >= w) break;
        x.push_back(0);
        y.push_back(y[i]+j+1);
      }
    }
    if(b-1==0){
      rep(j,h){
        if(x[i]+j+1 >= h) break;
        y.push_back(0);
        x.push_back(x[i]+j+1);
      }
    }
  }
  // for(auto hoge:x) cout << hoge << endl;
  // for(auto hoge:y) cout << hoge << endl;

  for (int i = 0; i < x.size(); i++)
  {
    for(int j = x[i]; j < h; ++j){
      up[j][y[i]] = true;
      // cout << "up: " << j << y[i] << endl;
    }
    for(int j = y[i]; j < w; ++j){
      side[x[i]][j] = true;
      // cout << "side: " << x[i] << j << endl;
    }
  }

  int bad_sum=0;
  rep(i,h) rep(j,w) {
    if(up[i][j]&&side[i][j]){
      bad_sum++;
      // cout << i << j << endl;
    } 
  }
  cout << h*w - bad_sum << endl;
  return 0;
}