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
  int n, x;
  cin >> n >> x;
  vector<int> b;
  rep(i,n){
    int a;
    cin >> a;
    if(a!=x){
      b.push_back(a);
    }
  }
  for(auto x: b){
    cout << x << " ";
  }
  cout << endl;
  return 0;
}