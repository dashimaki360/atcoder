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
  string s, t;
  cin >> s;
  cin >> t;
  int diff = ((s[0] - t[0]) + 26) % 26;
  rep(i, s.length()){
    int x = ((s[i] -  t[i]) +26) % 26;
    if(diff != x){
      cout << "No" << endl;
      return 0;
    }
  }
  cout << "Yes" << endl;
  return 0;
}