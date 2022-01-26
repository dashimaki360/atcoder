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
  int a, b, w;
  cin >> a >> b >> w;
  w *= 1000;
  if(b * (w/a) < w) 
  {
  cout << "UNSATISFIABLE" << endl;
  return 0;
  }
  int amari = w%b?1:0;
  cout << w/b+amari << " " << w/a << endl;
  return 0;
}