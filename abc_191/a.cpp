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
  int v, t, s, d;
  cin >> v >> t >> s >> d;
  string ans = "Yes";
  if(v*t<=d && d<=v*s){
    ans = "No";
  }

  cout << ans << endl;
  return 0;
}