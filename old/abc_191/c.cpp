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
  int h, w;
  cin >> h >> w;
  vector<string> x(h);
  rep(i,h) cin >> x[i];
  int ans = 0;
  rep(i,h-1) rep(j,w-1){
    int cnt = 0;
    if(x[i][j]=='#')  cnt++;
    if(x[i+1][j]=='#')  cnt++;
    if(x[i][j+1]=='#')  cnt++;
    if(x[i+1][j+1]=='#')  cnt++;
    if(cnt==1 || cnt ==3) ans++;
  }
  cout << ans << endl;
  return 0;
}