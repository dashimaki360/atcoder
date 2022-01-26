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
  int a, b;
  cin >> a >> b;
  a = a + b;
  int ans;
  if(a >= 15 && b>=8) ans = 1;
  else if(a >= 10 && b >= 3) ans = 2;
  else if(a >= 3) ans = 3;
  else ans = 4;

  cout << ans << endl;
  return 0;
}